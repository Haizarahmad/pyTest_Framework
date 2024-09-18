from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pageObjects.BasePage import BasePage
class AddAhliKariahPage(BasePage):

    txtName = (By.NAME, "name")
    txtAge = (By.NAME, "age")
    txtRelationship = (By.NAME, "marital")
    txtNationality = (By.NAME, "nationality")
    txtEmail = (By.NAME, "email")
    txtPhone = (By.NAME, "phone")
    txtAddress = (By.NAME, "address")
    btnAddAhliKariah = (By.XPATH, "/html/body/div[2]/div/div/form/button")
    btnUpdate = (By.NAME, "update")
    btnBack = (By.XPATH, "//a[contains(text(),'Kembali')]")
    toastMsg = (By.XPATH, "//div[@class='toast-body']/p")

    def __init__(self, driver):
        super().__init__(driver)

    def getTxtName(self):
        return self.find(*AddAhliKariahPage.txtName)

    def getTxtAge(self):
        return self.find(*AddAhliKariahPage.txtAge)

    def getTxtRelationship(self):
        return Select(self.find(*AddAhliKariahPage.txtRelationship))

    def getTxtNationality(self):
        return Select(self.find(*AddAhliKariahPage.txtNationality))

    def getTxtEmail(self):
        return self.find(*AddAhliKariahPage.txtEmail)

    def getTxtPhone(self):
        return self.find(*AddAhliKariahPage.txtPhone)

    def getTxtAddress(self):
        return self.find(*AddAhliKariahPage.txtAddress)

    def getBtnAddAhliKariah(self):
        return self.find(*AddAhliKariahPage.btnAddAhliKariah)

    def getBtnBack(self):
        return self.find(*AddAhliKariahPage.btnBack).click()

    def getBtnUpdate(self):
        return self.find(*AddAhliKariahPage.btnUpdate)

    def getToastMsg(self):
        return self.find(*AddAhliKariahPage.toastMsg)

    def clearAhliKariahForm(self):
        self.getTxtName().clear()
        self.getTxtAge().clear()
        self.getTxtEmail().clear()
        self.getTxtPhone().clear()
        self.getTxtAddress().clear()

    def fillAhliKariahForm(self, data):
        self.getTxtName().send_keys(data["Nama"])
        self.getTxtAge().send_keys(data["Umur"])
        self.getTxtRelationship().select_by_value(data["Hubungan"])
        self.getTxtNationality().select_by_value(data["Bangsa"])
        self.getTxtEmail().send_keys(data["Emel"])
        self.getTxtPhone().send_keys(data["Telefon"])
        self.getTxtAddress().send_keys(data["Alamat"])
        self.getBtnAddAhliKariah().click()

    def verifyAhliKariahForm(self, data):
        assert self.getTxtName().get_attribute("value") == data["Nama"]
        assert self.getTxtAge().get_attribute("value") == data["Umur"]
        assert self.getTxtRelationship().first_selected_option.get_attribute("value") == data["Hubungan"]
        assert self.getTxtNationality().first_selected_option.get_attribute("value") == data["Bangsa"]
        assert self.getTxtEmail().get_attribute("value") == data["Emel"]
        assert self.getTxtPhone().get_attribute("value") == data["Telefon"]
        assert self.getTxtAddress().get_attribute("value") == data["Alamat"]

