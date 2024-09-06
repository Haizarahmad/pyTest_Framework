from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.AdminDashboardPage import AdminDashboardPage
from pageObjects.Admin.AhliKariahPage import AhliKariahPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
import time

class TestAhliKariah(BaseClass):

    def test_navigateToAhliKariah(self):
        try:
            loginpage = LoginPage(self.driver)
            self.driver.get("http://localhost/MDUMS/Masjid%20Darul%20Ulum%20-%20Ver2/New-Login-Page.php")
            self.driver.maximize_window()
            loginpage.getUsername().send_keys("admin")  # Replace with actual admin username
            loginpage.getPassword().send_keys("123")  # Replace with actual admin password
            loginpage.performLogin()  # Perform login action
            time.sleep(2)
            loginpage.acceptAlert()
            time.sleep(2)
            adminDashboard = AdminDashboardPage(self.driver)
            adminDashboard.getAhliKariah().click()
        except Exception:
            raise Exception

    def test_addAhliKariah(self):
        try:
            ahliKariahPage = AhliKariahPage(self.driver)
            ahliKariahPage.getBtnAddAhliKariah().click()
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.getTxtName().send_keys("ahmad")
            addAhliKariahPage.getTxtAge().send_keys("12")
            addAhliKariahPage.getTxtRelationship().send_keys("Bujang")
            addAhliKariahPage.getTxtNationality().send_keys("Melayu")
            addAhliKariahPage.getTxtEmail().send_keys("haizar@gmail.com")
            addAhliKariahPage.getTxtPhone().send_keys("013-44556978")
            addAhliKariahPage.getTxtAddress().send_keys("SL/51 Lorong Juara 3J")
            time.sleep(2)
            addAhliKariahPage.getBtnAddAhliKariah().click()
            time.sleep(2)
        except Exception:
            raise Exception

    # def test_deleteAhliKariah(self):
    #     pass
    #
    # def test_updateAhliKariah(self):
    #     pass
    #
    # def test_readAhliKariah(self):
    #     pass