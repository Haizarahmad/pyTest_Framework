import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()  # Open Chrome Driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
