from selenium.webdriver.common.by import By

from pageObjects.Admin.AddAhliKariahPage import AddAhliKariahPage


class UpdateAhliKariahPage:

    btnUpdate = (By.XPATH, "//button[contains(text(),'Kemaskini')]")
    toastMsg = (By.XPATH, "//div[@class='toast-body']/p")
    def __init__(self, driver):
        self.driver = driver

    def getBtnUpdate(self):
        return self.driver.find_element(*UpdateAhliKariahPage.btnUpdate)

    def getToastMsg(self):
        return self.driver.find_element(*UpdateAhliKariahPage.toastMsg)

    def UpdateAhliKariahForm(self, data):
        fieldElement = AddAhliKariahPage(self.driver)
        fieldElement.getTxtName().clear()
        fieldElement.getTxtName().send_keys(data["updNama"])
        fieldElement.getTxtAge().clear()
        fieldElement.getTxtAge().send_keys(data["updUmur"])
        fieldElement.getTxtRelationship().select_by_value(data["updHubungan"])
        fieldElement.getTxtNationality().select_by_value(data["updBangsa"])
        fieldElement.getTxtEmail().clear()
        fieldElement.getTxtEmail().send_keys(data["updEmel"])
        fieldElement.getTxtPhone().clear()
        fieldElement.getTxtPhone().send_keys(data["updTelefon"])
        fieldElement.getTxtAddress().clear()
        fieldElement.getTxtAddress().send_keys(data["updAlamat"])
        self.driver.find_element(*UpdateAhliKariahPage.btnUpdate).click()

    def verifyUpdatedAhliKariahForm(self, data):
        updatedFieldElements = AddAhliKariahPage(self.driver)
        assert updatedFieldElements.getTxtName().get_attribute("value") == data["updNama"]
        assert updatedFieldElements.getTxtAge().get_attribute("value") == data["updUmur"]
        assert updatedFieldElements.getTxtRelationship().first_selected_option.get_attribute("value") == data["updHubungan"]
        assert updatedFieldElements.getTxtNationality().first_selected_option.get_attribute("value") == data["updBangsa"]
        assert updatedFieldElements.getTxtEmail().get_attribute("value") == data["updEmel"]
        assert updatedFieldElements.getTxtPhone().get_attribute("value") == data["updTelefon"]
        assert updatedFieldElements.getTxtAddress().get_attribute("value") == data["updAlamat"]
