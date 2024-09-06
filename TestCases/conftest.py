import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage


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

    request.cls.driver = driver
    yield
    driver.close()