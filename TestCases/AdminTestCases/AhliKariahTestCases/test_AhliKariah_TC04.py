import pytest

from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.SideBar import SideBar
from utilities.BaseClass import BaseClass
import time
@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):
    @pytest.mark.functional
    def test_TC04(self, getValidData):
        try:

            #origanal LOC: 13

            # Navigate to Ahli Kariah Module#
            sideBar = SideBar(self.driver)
            ahliKariahPage = sideBar.getAhliKariah()
            time.sleep(2)

            # To add Test Data #
            self.clickByElement(ahliKariahPage.getBtnAddAhliKariah())
            time.sleep(2)
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.fillAhliKariahForm(getValidData)

            # To search Test Data #
            addAhliKariahPage.getBtnBack()
            time.sleep(2)
            self.enterTextByElement(ahliKariahPage.getTxtSearchAhliKariah(), getValidData["NameSearch"])
            time.sleep(2)

            # To delete Test Data #
            ahliKariahPage.delAhliKariahByName(getValidData["DelByName"])

        except Exception:
            raise
    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC04.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
