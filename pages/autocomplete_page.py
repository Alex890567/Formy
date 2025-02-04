from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AutocompletePage:
    def __init__(self, driver, navigation_page):
        self.driver = driver
        self.Navigation_Page = navigation_page
        self.Address = (By.ID, "autocomplete")


    def send_keys_to_address(self):
        self.Navigation_Page.go_to_autocomplete()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.Address))
        element.send_keys("Mountain View")
        return element.get_attribute("value")
