from selenium.webdriver.common.by import By

from pageObjects.Admin.AhliKariahPage import AhliKariahPage


class SideBar:

    linkUtama = (By.LINK_TEXT, "Utama")
    linkAhliKariah = (By.LINK_TEXT, "Ahli Kariah")
    linkNotifikasi = (By.LINK_TEXT, "Notifikasi")
    linkLogKeluar = (By.LINK_TEXT, "Log Keluar")

    def __init__(self, driver):
        self.driver = driver

    def getUtama(self):
        return self.driver.find_element(*SideBar.linkUtama)

    def getAhliKariah(self):
        self.driver.find_element(*SideBar.linkAhliKariah).click()
        ahliKariahPage = AhliKariahPage(self.driver)
        return ahliKariahPage

    def getNotifikasi(self):
        return self.driver.find_element(*SideBar.linkNotifikasi)

    def getLogKeluar(self):
        return self.driver.find_element(*SideBar.linkLogKeluar)
