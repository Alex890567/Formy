from selenium.webdriver.common.by import By


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.Autocomplete = (By.XPATH, "//a[@class='btn btn-lg' and @href='/autocomplete']")


    def go_to_autocomplete(self):
        element = self.driver.find_element(*self.Autocomplete)
        element.click()
        return self.driver.current_url