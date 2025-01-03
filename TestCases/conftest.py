#pytest --html=report/report.html --self-contained-html -q
#pytest --browser_name chrome --html=report/report.html --self-contained-html
import time
import os
import pytest
from selenium import webdriver

from MantisBugTracker.MantisBugTracker import MantisBugTracker
from utilities.BaseClass import BaseClass
import re

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    try:
        browser_name = request.config.getoption("browser_name")

        if browser_name == "chrome":
            driver = webdriver.Chrome()  # Open Chrome Driver
        elif browser_name == "firefox":
            driver = webdriver.Firefox()

        request.cls.driver = driver
        request.cls.driver.maximize_window()
        yield
        driver.quit()  # Ensure the browser session is properly ended
    except Exception as e:
        raise Exception(f"Unable to setup browser: {str(e)}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global exception_message
    LogIssue = MantisBugTracker(2)
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extras = getattr(report, "extras", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")

        # if any test cases fail this block will occur #
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure #
            # Generate the screenshot filename and folder #
            file_name = sanitize_filename(report.nodeid.replace("::", "_") + ".png")
            report_folder = os.path.join(os.getcwd(), "report")
            screenshot_folder = os.path.join(report_folder, "screenshots")

            # Create the screenshots directory if it doesn't exist #
            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)

            # Save the screenshot #
            screenshot_path = os.path.join(screenshot_folder, file_name)

            # Capture the screenshot #
            _capture_screenshot(screenshot_path, driver)

            # Use relative path for the screenshot in the HTML report #
            relative_path = os.path.relpath(screenshot_path, report_folder)
            if relative_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px; height:228px;" '\
                       'onclick="window.open(this.src)" align="right"/></div>' % relative_path
                extras.append(pytest_html.extras.html(html))

            exception_message = str(call.excinfo.value) if call.excinfo else "No exception message"

            # Log the issue in Mantis #
            TypofErr = "Control Flow"
            TypeOfErr = f"Type of Error: {TypofErr}"
            TestCaseName = getTestCaseName(report.nodeid)
            summary = f"Test Case Failed: {TestCaseName}"  # Test case name as summary
            description = f"{TypeOfErr}\n\nException Details: {exception_message}"  # Exception details as description
            LogIssue.log_issue(summary, description)

        report.extras = extras

def sanitize_filename(filename):
    # Replace special characters with underscores for better file naming
    return re.sub(r'[^A-Za-z0-9._-]', '_', filename)

def getTestCaseName(filePath):
    match = re.search(r'/([^/]+)\.py', filePath)

    if match:
        result = match.group(1)
        return result

def _capture_screenshot(name, driver):
    driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "[SWT-20231101-0001] MDUMS Automation Test Report"

@pytest.fixture(scope="class")
def loginAsAdmin(setup, request):
    # Common setup logic for all test cases
    loginPage = BaseClass()
    loginPage.loginAsAdmin(request.cls.driver)  # Use the driver from the class fixture
    time.sleep(2)
    yield
