from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AutocompletePage:
    def __init__(self, driver, navigation_page):
        self.driver = driver
        self.Navigation_Page = navigation_page
        self.wait = WebDriverWait(self.driver, 10)
        self.Address = (By.ID, "autocomplete")
        self.Street_Address = (By.ID, "street_number")


    def send_keys_to_address(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.Address))
        element.send_keys("Mountain View")
        return element.get_attribute("value")

    def send_keys_to_street_address(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.Street_Address))
        element.send_keys("Mountain View 23")
        return element.get_attribute("value")
