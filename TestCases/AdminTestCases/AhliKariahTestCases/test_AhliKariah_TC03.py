import pytest
from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.SideBar import SideBar
from utilities.BaseClass import BaseClass
import time

@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):

    @pytest.mark.functional
    def test_TC03(self, getValidData):

        try:
            # step navigate to Ahli Kariah module #
            sideBar = SideBar(self.driver)
            ahliKariahPage = sideBar.getAhliKariah()
            self.clickByElement(ahliKariahPage.getBtnAddAhliKariah())
            time.sleep(2)

            # Add data #
            addAhlikariahPage = AddAhliKariahPage(self.driver)
            addAhlikariahPage.fillAhliKariahForm(getValidData)
            addAhlikariahPage.getBtnBack()
            time.sleep(2)

            # search data #
            self.enterTextByElement(ahliKariahPage.getTxtSearchAhliKariah(), getValidData["NameSearch"])
            time.sleep(2)

            # view data #
            ahliKariahPage.viewAhliKariahByName(getValidData["NameSearch"])
            time.sleep(2)

            # verify data #
            addAhlikariahPage.verifyAhliKariahForm(getValidData)
            time.sleep(2)
        except Exception:
            raise
        finally:
            time.sleep(2)
            self.dataCleanup(getValidData["Nama"], self.driver)

    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC03.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
