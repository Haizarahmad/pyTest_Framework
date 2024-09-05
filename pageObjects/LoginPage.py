from selenium.webdriver.common.by import By


class LoginPage:

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "login")

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def performLogin(self):
        return self.driver.find_element(*LoginPage.login_button).click()