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
        self.Street_Address_2 = (By.ID, "route")
        self.City = (By.ID, "locality")
        self.State = (By.ID, "administrative_area_level_1")
        self.Zip_Code = (By.ID, "postal_code")


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

    def send_keys_to_street_address_2(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.Street_Address_2))
        element.send_keys("Plain View 20")
        return element.get_attribute("value")

    def send_keys_to_city(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.City))
        element.send_keys("Houston")
        return element.get_attribute("value")

    def send_keys_to_state(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.State))
        element.send_keys("Texas")
        return element.get_attribute("value")

    def send_keys_to_zip_code(self):
        self.Navigation_Page.go_to_autocomplete()
        element = self.wait.until(EC.presence_of_element_located(self.Zip_Code))
        element.send_keys("1234")
        return element.get_attribute("value")
