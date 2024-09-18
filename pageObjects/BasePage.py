class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        #self.find(*AddAhliKariahPage.txtNationality)
        return self.driver.find_element(*locator)

    def clear(self, *locator):
        return self.driver.find_element(*locator).clear()
