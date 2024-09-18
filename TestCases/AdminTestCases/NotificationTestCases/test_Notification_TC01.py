import pytest

from TestData.Notifikasi.NotificationPageData import NotificationPageData
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("loginAsAdmin")
class TestNotification(BaseClass):

    def test_TC01(self):

        try:
            pass
        except:
            pass

    @pytest.fixture(params=NotificationPageData.getData(""))
    def getValidData(self, request):
        return request.params