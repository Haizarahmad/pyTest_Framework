import inspect
import logging
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Admin.SideBar import SideBar
from pageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    loginPageURL = "http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php"
    def verifyPresence(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def clickByElement(self, locator):
        try:
            return locator.click()
        except Exception:
            raise Exception("Unable to locate/click the element")
    def enterTextByElement(self, locator, text):
        try:
            return locator.send_keys(text)
        except Exception:
            raise Exception("Unable to locate or send input to the element")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger

    def loginAsAdmin(self, driver):
        try:
            self.driver = driver
            loginpage = LoginPage(self.driver)
            self.driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
            self.enterTextByElement(loginpage.getUsername(), "admin")  # Replace with actual admin username
            self.enterTextByElement(loginpage.getPassword(), "123")
            loginpage.performLogin()  # Perform login action
            time.sleep(2)
            loginpage.acceptAlert()
            time.sleep(2)
        except Exception:
            raise Exception("Unable login")

    def dataCleanup(self, data, driver):
        sideBar = SideBar(driver)
        ahliKariahPage = sideBar.getAhliKariah()
        self.enterTextByElement(ahliKariahPage.getTxtSearchAhliKariah(), data)
        ahliKariahPage.delAhliKariahByName(data)
        time.sleep(2)



