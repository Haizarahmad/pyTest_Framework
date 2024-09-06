from selenium.webdriver.common.by import By


class LoginPage:

    txtUsername = (By.ID, "username")
    txtPassword = (By.ID, "password")
    btnLogin = (By.ID, "login")

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        return self.driver.find_element(*LoginPage.txtUsername) #* to unpack the tuple

    def getPassword(self):
        return self.driver.find_element(*LoginPage.txtPassword)

    def acceptAlert(self):
        return self.driver.switch_to.alert.accept()
    def getSuccessMessage(self):
        return self.driver.switch_to.alert.text

    def getFailedMessage(self):
        return self.driver.switch_to.alert.text

    def performLogin(self):
        return self.driver.find_element(*LoginPage.btnLogin).click()
