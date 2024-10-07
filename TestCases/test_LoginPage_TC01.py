import pytest
import time
from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    @pytest.mark.smoke
    def test_TC01(self, getValidData):
        try:
            self.driver.implicitly_wait(3)
            self.driver.get(self.loginPageURL)
            self.driver.maximize_window()
            loginpage = LoginPage(self.driver)
            loginpage.getUsername().clear()
            loginpage.getUsername().send_keys(getValidData["username"])
            loginpage.getPassword().send_keys(getValidData["password"])
            loginpage.performLogin()
            time.sleep(2)
            alert_message = loginpage.getSuccessMessage()
            time.sleep(2)
            loginpage.acceptAlert()
            assert alert_message == "You have been successfully log in", "Message is not match"
            self.driver.back()
        except:
            log = self.getLogger()
            log.critical("Failed")
            raise

    @pytest.mark.functional
    def test_invalid_login_submission(self, getInvalidData):
        try:
            self.driver.implicitly_wait(3)
            self.driver.get(self.loginPageURL)
            self.driver.maximize_window()
            loginpage = LoginPage(self.driver)
            loginpage.getUsername().clear()
            loginpage.getUsername().send_keys(getInvalidData["username"])
            loginpage.getPassword().send_keys(getInvalidData["password"])
            loginpage.performLogin()
            time.sleep(2)
            alert_message = loginpage.getFailedMessage()
            time.sleep(2)
            loginpage.acceptAlert()
            assert alert_message == getInvalidData["ExpectedResult"], "Message is not match"
            self.driver.back()
        except:
            log = self.getLogger()
            log.critical("Failed")
            raise

    @pytest.fixture(params=LoginPageData.getValidData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\testdata_TC01.xlsx")) #one tuple represent one test case
    def getValidData(self, request):
        return request.param

    @pytest.fixture(params=LoginPageData.test_LoginPage_invalid_data) #one tuple represent one test case
    # [{"username": "amin", "password": "13", "ExpectedResult": "n/a"}]
    def getInvalidData(self, request):
        return request.param

