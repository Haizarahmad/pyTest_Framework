import pytest

from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.AdminDashboardPage import AdminDashboardPage
from pageObjects.Admin.AhliKariahPage import AhliKariahPage
from utilities.BaseClass import BaseClass
import time
@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):
    @pytest.mark.regression
    def test_deleteAhliKariah(self, getValidData):
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
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["NameSearch"])
            time.sleep(2)
            ahliKariahPage.delAhliKariahByName(getValidData["DelByName"])
        except Exception:
            raise Exception
    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC04.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
