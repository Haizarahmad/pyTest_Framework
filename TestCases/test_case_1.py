from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time
from pageObjects.LoginPage import LoginPage
import pytest


class TestCase1(BaseClass):

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.fill_username().send_keys("admin")
        time.sleep(2)
        loginpage.fill_password().send_keys("123")
        time.sleep(2)
        loginpage.login().click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)


