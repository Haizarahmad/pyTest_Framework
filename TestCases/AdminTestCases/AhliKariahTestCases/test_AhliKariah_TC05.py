import pytest

from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.AdminDashboardPage import AdminDashboardPage
from pageObjects.Admin.AhliKariahPage import AhliKariahPage
from pageObjects.Admin.UpdateAhliKariahPage import UpdateAhliKariahPage
from utilities.BaseClass import BaseClass
import time



@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):
    @pytest.mark.regression
    def test_updateAhliKariah(self, getValidData):

        global addAhliKariahPage, ahliKariahPage
        try:
            adminDashboard = AdminDashboardPage(self.driver)
            adminDashboard.getAhliKariah().click()
            time.sleep(2)
            ahliKariahPage = AhliKariahPage(self.driver)
            ahliKariahPage.getBtnAddAhliKariah().click()
            time.sleep(2)
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.fillAhliKariahForm(getValidData)
            addAhliKariahPage.getBtnBack().click()
            time.sleep(2)
            #search data
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["NameSearch"])
            time.sleep(2)
            ahliKariahPage.viewAhliKariahByName(getValidData["NameSearch"])
            #update steps
            updateAhliKariahPage = UpdateAhliKariahPage(self.driver)
            time.sleep(2)
            updateAhliKariahPage.UpdateAhliKariahForm(getValidData)
            time.sleep(2)
            addAhliKariahPage.getBtnBack().click()
            time.sleep(2)
            #verify data steps
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["updNama"])
            time.sleep(2)
            ahliKariahPage.viewAhliKariahByName(getValidData["updNama"])
            time.sleep(2)
            updateAhliKariahPage.verifyUpdatedAhliKariahForm(getValidData)
        except Exception:
            raise Exception
        finally:
            time.sleep(2)
            addAhliKariahPage.getBtnBack().click()
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["updNama"])
            ahliKariahPage.delAhliKariahByName(getValidData["updNama"])
    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC05.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
