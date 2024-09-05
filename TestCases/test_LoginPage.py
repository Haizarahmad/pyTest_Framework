import time

import pytest

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):

    def test_loginsubmission(self, getData):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.getUsername().clear()
        loginpage.getUsername().send_keys(getData["username"])
        log.info("Username Entered")
        time.sleep(2)
        loginpage.getPassword().send_keys(getData["password"])
        log.info("Password Entered")
        time.sleep(2)
        loginpage.performLogin()
        log.info("logged in")
        time.sleep(2)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        self.driver.back()

    @pytest.fixture(params=LoginPageData.test_LoginPage_data) #one tuple represent one test case
    def getData(self, request):
        return request.param

