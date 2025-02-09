from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonsPage:
    def __init__(self, driver, navigation_page):
        self.driver = driver
        self.Navigation_page = navigation_page
        self.wait = WebDriverWait(self.driver, 10)
        self.Primary = (By.XPATH, "(//button[@class='btn btn-lg btn-primary'])[1]")


    def click_primary_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Primary))
        element.click()
        return element
