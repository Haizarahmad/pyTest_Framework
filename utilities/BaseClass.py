import inspect
import logging
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyPresence(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

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
        self.driver = driver
        loginpage = LoginPage(self.driver)
        self.driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
        self.driver.maximize_window()
        loginpage.getUsername().send_keys("admin")  # Replace with actual admin username
        loginpage.getPassword().send_keys("123")  # Replace with actual admin password
        loginpage.performLogin()  # Perform login action
        time.sleep(2)
        loginpage.acceptAlert()
        time.sleep(2)



