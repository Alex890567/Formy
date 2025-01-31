from selenium.webdriver.common.by import By


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.Autocomplete = (By.XPATH, "//a[@class='btn btn-lg' and @href='/autocomplete']")
        self.Buttons = (By.XPATH, "//a[@class='btn btn-lg' and @href='/buttons']")
        self.Checkbox = (By.XPATH, "//a[@class='btn btn-lg' and @href='/checkbox']")
        self.Datepicker = (By.XPATH, "//a[@class='btn btn-lg' and @href='/datepicker']")
        self.Drag_and_Drop = (By.XPATH, "//a[@class='btn btn-lg' and @href='/dragdrop']")
        self.Enabled_and_Disabled_Elements = (By.XPATH, "//a[@class='btn btn-lg' and @href='/enabled']")

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

    def go_to_drag_and_drop(self):
        element = self.driver.find_element(*self.Drag_and_Drop)
        element.click()
        return self.driver.current_url

    def go_to_enabled_and_disabled_elements(self):
        element = self.driver.find_element(*self.Enabled_and_Disabled_Elements)
        element.click()
        return self.driver.current_url
