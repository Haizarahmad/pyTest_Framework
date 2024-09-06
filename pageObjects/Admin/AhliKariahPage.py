from selenium.webdriver.common.by import By


class AhliKariahPage:

    btnAddAhliKariah = (By.LINK_TEXT, "Tambah")
    btnViewAhliKariah = (By.LINK_TEXT, "Lihat")
    btnDelAhliKariah = (By.LINK_TEXT, "Padam")
    def __init__(self, driver):
        self.driver = driver
    def getBtnAddAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnAddAhliKariah)

    def getBtnViewAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnViewAhliKariah)

    def getBtnDelAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnDelAhliKariah)


