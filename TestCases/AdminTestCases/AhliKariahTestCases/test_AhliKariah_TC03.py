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
    def test_readAhliKariah(self, getValidData):

        global addAhlikariahPage, ahliKariahPage
        try:
            adminDashboard = AdminDashboardPage(self.driver)
            adminDashboard.getAhliKariah().click()
            ahliKariahPage = AhliKariahPage(self.driver)
            ahliKariahPage.getBtnAddAhliKariah().click()
            time.sleep(2)
            addAhlikariahPage = AddAhliKariahPage(self.driver)
            addAhlikariahPage.fillAhliKariahForm(getValidData)
            addAhlikariahPage.getBtnBack().click()
            time.sleep(2)
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["NameSearch"])
            time.sleep(2)
            ahliKariahPage.viewAhliKariahByName(getValidData["NameSearch"])
            time.sleep(2)
            addAhlikariahPage.verifyAhliKariahForm(getValidData)
            time.sleep(2)
        except Exception:
            raise Exception
        finally:
            time.sleep(2)
            addAhlikariahPage.getBtnBack().click()
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["NameSearch"])
            ahliKariahPage.delAhliKariahByName(getValidData["NameSearch"])

    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC03.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
