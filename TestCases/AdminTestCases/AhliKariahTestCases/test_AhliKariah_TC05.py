import pytest
from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.SideBar import SideBar
from utilities.BaseClass import BaseClass
import time


@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):
    @pytest.mark.functional
    def test_TC05(self, getValidData):

        try:
            # Navigate to Ahli Kariah Module #
            sideBar = SideBar(self.driver)
            ahliKariahPage = sideBar.getAhliKariah()

            # To add test data #
            self.clickByElement(ahliKariahPage.getBtnAddAhliKariah())
            time.sleep(2)
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.fillAhliKariahForm(getValidData)
            addAhliKariahPage.getBtnBack()
            time.sleep(2)

            # Search Test data #
            self.enterTextByElement(ahliKariahPage.getTxtSearchAhliKariah(), getValidData["NameSearch"])
            time.sleep(2)

            # Update Test Data#
            updateAhliKariahPage = ahliKariahPage.viewAhliKariahByName(getValidData["NameSearch"])
            time.sleep(2)
            updateAhliKariahPage.UpdateAhliKariahForm(getValidData)
            time.sleep(2)

            # Search Updated Test Data #
            updateAhliKariahPage.getBtnBack()
            self.enterTextByElement(ahliKariahPage.getTxtSearchAhliKariah(), getValidData["updNama"])
            time.sleep(2)
            ahliKariahPage.viewAhliKariahByName(getValidData["updNama"])
            time.sleep(2)

            # Verify Updated Test Data #
            updateAhliKariahPage.verifyUpdatedAhliKariahForm(getValidData)
        except Exception:
            raise Exception("Unable to update existing data")
        finally:
            time.sleep(2)
            self.dataCleanup(getValidData["updNama"], self.driver)
    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC05.xlsx")) #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
