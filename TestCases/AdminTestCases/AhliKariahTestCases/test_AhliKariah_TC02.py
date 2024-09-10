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
    def test_addAhliKariah(self, getValidData):

        global addAhliKariahPage, ahliKariahPage
        try:

            adminDashboard = AdminDashboardPage(self.driver)
            adminDashboard.getAhliKariah().click()
            ahliKariahPage = AhliKariahPage(self.driver)
            ahliKariahPage.getBtnAddAhliKariah().click()
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.fillAhliKariahForm(getValidData)
            time.sleep(1)
            toast = addAhliKariahPage.getToastMsg().text
            time.sleep(2)
            assert toast == getValidData["ToastMsg"]
            time.sleep(2)
        except Exception:
            raise Exception
        finally:
            addAhliKariahPage.getBtnBack().click()
            time.sleep(2)
            ahliKariahPage.getTxtSearchAhliKariah().send_keys(getValidData["Nama"])
            ahliKariahPage.delAhliKariahByName(getValidData["Nama"])

    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC02.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
