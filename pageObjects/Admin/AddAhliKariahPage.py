from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddAhliKariahPage:

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
        self.driver = driver

    def getTxtName(self):
        return self.driver.find_element(*AddAhliKariahPage.txtName)

    def getTxtAge(self):
        return self.driver.find_element(*AddAhliKariahPage.txtAge)

    def getTxtRelationship(self):
        return Select(self.driver.find_element(*AddAhliKariahPage.txtRelationship))

    def getTxtNationality(self):
        return Select(self.driver.find_element(*AddAhliKariahPage.txtNationality))

    def getTxtEmail(self):
        return self.driver.find_element(*AddAhliKariahPage.txtEmail)

    def getTxtPhone(self):
        return self.driver.find_element(*AddAhliKariahPage.txtPhone)

    def getTxtAddress(self):
        return self.driver.find_element(*AddAhliKariahPage.txtAddress)

    def getBtnAddAhliKariah(self):
        return self.driver.find_element(*AddAhliKariahPage.btnAddAhliKariah)

    def getBtnBack(self):
        return self.driver.find_element(*AddAhliKariahPage.btnBack)

    def getBtnUpdate(self):
        return self.driver.find_element(*AddAhliKariahPage.btnUpdate)

    def getToastMsg(self):
        return self.driver.find_element(*AddAhliKariahPage.toastMsg)

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

