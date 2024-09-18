import time
from selenium.webdriver.common.by import By

from pageObjects.Admin.UpdateAhliKariahPage import UpdateAhliKariahPage


class AhliKariahPage:

    btnAddAhliKariah = (By.LINK_TEXT, "Tambah")
    btnViewAhliKariah = (By.XPATH, "td[6]/a")
    btnDelAhliKariah = (By.XPATH, "td[6]/button")
    txtSearch = (By.XPATH, "//div[contains(@id, 'example_filter')]/label/input")
    table = (By.XPATH, "//table/tbody")
    modal = (By.XPATH, "//div[2]/div/div[contains(@class, 'modal fade show')]/div[contains(@class, 'modal-dialog')]")
    modalbtnDel = (By.XPATH, "//div[2]/div/div[contains(@class, 'modal fade show')]/div/div/div[contains(@class,'modal-footer')]/a")
    def __init__(self, driver):
        self.driver = driver

    def getBtnAddAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnAddAhliKariah)

    def getBtnViewAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnViewAhliKariah)

    def getBtnDelAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.btnDelAhliKariah)

    def getTxtSearchAhliKariah(self):
        return self.driver.find_element(*AhliKariahPage.txtSearch)

    def viewAhliKariahByName(self, name):
        try:
            elements = self.driver.find_elements(*AhliKariahPage.table)
            for element in elements:
                target_element = element.find_element(By.XPATH, f"tr[contains(.,'{name}')]")
                if target_element is not None:
                    target_element.find_element(*AhliKariahPage.btnViewAhliKariah).click()
                    updateAhliKariahPage = UpdateAhliKariahPage(self.driver)
                    return updateAhliKariahPage
        except Exception:
            raise Exception("Unable to view data by Name")

    def delAhliKariahByName(self, name):
        elements = self.driver.find_elements(*AhliKariahPage.table)
        for element in elements:
            target_element = element.find_element(By.XPATH, f"tr[contains(.,'{name}')]")
            if target_element is not None:
                target_element.find_element(*AhliKariahPage.btnDelAhliKariah).click()
                time.sleep(2)
                return self.driver.find_element(*AhliKariahPage.modalbtnDel).click()


















