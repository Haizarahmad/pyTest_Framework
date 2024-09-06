from selenium.webdriver.common.by import By


class AddAhliKariahPage:

    txtName = (By.NAME, "name")
    txtAge = (By.NAME, "age")
    txtRelationship = (By.NAME, "marital")
    txtNationality = (By.NAME, "nationality")
    txtEmail = (By.NAME, "email")
    txtPhone = (By.NAME, "phone")
    txtAddress = (By.NAME, "address")
    btnAddAhliKariah = (By.XPATH, "/html/body/div[2]/div/div/form/button")
    def __init__(self, driver):
        self.driver = driver
    def getTxtName(self):
        return self.driver.find_element(*AddAhliKariahPage.txtName)

    def getTxtAge(self):
        return self.driver.find_element(*AddAhliKariahPage.txtAge)

    def getTxtRelationship(self):
        return self.driver.find_element(*AddAhliKariahPage.txtRelationship)

    def getTxtNationality(self):
        return self.driver.find_element(*AddAhliKariahPage.txtNationality)

    def getTxtEmail(self):
        return self.driver.find_element(*AddAhliKariahPage.txtEmail)

    def getTxtPhone(self):
        return self.driver.find_element(*AddAhliKariahPage.txtPhone)

    def getTxtAddress(self):
        return self.driver.find_element(*AddAhliKariahPage.txtAddress)

    def getBtnAddAhliKariah(self):
        return self.driver.find_element(*AddAhliKariahPage.btnAddAhliKariah)