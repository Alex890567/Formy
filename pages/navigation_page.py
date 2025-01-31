from selenium.webdriver.common.by import By


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.Autocomplete = (By.XPATH, "//a[@class='btn btn-lg' and @href='/autocomplete']")
        self.Buttons = (By.XPATH, "//a[@class='btn btn-lg' and @href='/buttons']")
        self.Checkbox = (By.XPATH, "//a[@class='btn btn-lg' and @href='/checkbox']")
        self.Datepicker = (By.XPATH, "//a[@class='btn btn-lg' and @href='/datepicker']")

    def go_to_autocomplete(self):
        element = self.driver.find_element(*self.Autocomplete)
        element.click()
        return self.driver.current_url

    def go_to_buttons(self):
        element = self.driver.find_element(*self.Buttons)
        element.click()
        return self.driver.current_url

    def go_to_checkbox(self):
        element = self.driver.find_element(*self.Checkbox)
        element.click()
        return self.driver.current_url

    def go_to_datepicker(self):
        element = self.driver.find_element(*self.Datepicker)
        element.click()
        return self.driver.current_url
