import pytest
import time
from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):

    def test_valid_login_submission(self, getValidData):
        self.driver.implicitly_wait(3)
        self.driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
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
        assert alert_message == getValidData["ExpectedResult"], "Message is not match"
        self.driver.back()

    def test_invalid_login_submission(self, getInvalidData):
        self.driver.implicitly_wait(3)
        self.driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
        self.driver.maximize_window()
        # log = self.getLogger()
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

    @pytest.fixture(params=LoginPageData.test_LoginPage_valid_data) #one tuple represent one test case
    def getValidData(self, request):
        return request.param

    @pytest.fixture(params=LoginPageData.test_LoginPage_invalid_data) #one tuple represent one test case
    def getInvalidData(self, request):
        return request.param

