from selenium.webdriver.common.by import By


class AdminDashboardPage:

    linkUtama = (By.LINK_TEXT, "Utama")
    linkAhliKariah = (By.LINK_TEXT, "Ahli Kariah")
    linkNotifikasi = (By.LINK_TEXT, "Notifikasi")
    linkLogKeluar = (By.LINK_TEXT, "Log Keluar")

    def __init__(self, driver):
        self.driver = driver

    def getUtama(self):
        return self.driver.find_element(*AdminDashboardPage.linkUtama)

    def getAhliKariah(self):
        return self.driver.find_element(*AdminDashboardPage.linkAhliKariah)

    def getNotifikasi(self):
        return self.driver.find_element(*AdminDashboardPage.linkNotifikasi)

    def getLogKeluar(self):
        return self.driver.find_element(*AdminDashboardPage.linkLogKeluar)


