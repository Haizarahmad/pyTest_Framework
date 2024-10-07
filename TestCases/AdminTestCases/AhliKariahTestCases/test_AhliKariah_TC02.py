import pytest

from TestData.AhliKariah.AhliKariahPageData import AhliKariahPageData
from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage
from pageObjects.Admin.SideBar import SideBar
from utilities.BaseClass import BaseClass
import time

@pytest.mark.usefixtures("loginAsAdmin")
class TestAhliKariah(BaseClass):

    @pytest.mark.smoke
    def test_TC02(self, getValidData):

        try:
            # To navigate Ahli Kariah module #
            sideBar = SideBar(self.driver)
            ahliKariahPage = sideBar.getAhliKariah()

            # to go adding data
            self.clickByElement(ahliKariahPage.getBtnAddAhliKariah())

            # To add test data #
            addAhliKariahPage = AddAhliKariahPage(self.driver)
            addAhliKariahPage.fillAhliKariahForm(getValidData)
            time.sleep(1)
            toast = addAhliKariahPage.getToastMsg().text
            time.sleep(2)
            assert toast == getValidData["ToastMsg"], f'Message does not match' \
                                                      f'\nExpect: {getValidData["ToastMsg"]}' \
                                                      f'\nActual result: {toast}'
        except Exception as ex:
            raise Exception(str(ex))

        # data cleanup #
        time.sleep(2)
        self.dataCleanup(getValidData["Nama"], self.driver)

    @pytest.fixture(params=AhliKariahPageData.getData("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\AhliKariah\\testdata_TC02.xlsx"))
    #data passed always in params = []  # one tuple represent one test case
    def getValidData(self, request):
        return request.param
