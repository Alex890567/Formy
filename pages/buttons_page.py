from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonsPage:
    def __init__(self, driver, navigation_page):
        self.driver = driver
        self.Navigation_page = navigation_page
        self.wait = WebDriverWait(self.driver, 10)
        self.Primary = (By.XPATH, "(//button[@class='btn btn-lg btn-primary'])[1]")
        self.Success = (By.XPATH, "//button[@class='btn btn-lg btn-success']")
        self.Info = (By.XPATH, "//button[@class='btn btn-lg btn-info']")
        self.Warning = (By.XPATH, "//button[@class='btn btn-lg btn-warning']")
        self.Danger = (By.XPATH, "//button[@class='btn btn-lg btn-danger']")
        self.Link = (By.XPATH, "//button[@class='btn btn-lg btn-link']")
        self.Left = (By.XPATH, "(//button[@class='btn btn-lg btn-primary'])[2]")
        self.Middle = (By.XPATH, "(//button[@class='btn btn-lg btn-primary'])[3]")
        self.Right = (By.XPATH, "(//button[@class='btn btn-lg btn-primary'])[4]")

    def click_primary_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Primary))
        element.click()
        return element

    def click_success_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Success))
        element.click()
        return element

    def click_info_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Info))
        element.click()
        return element

    def click_warning_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Warning))
        element.click()
        return element

    def click_danger_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Danger))
        element.click()
        return element

    def click_link_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Link))
        element.click()
        return element

    def click_left_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Left))
        element.click()
        return element

    def click_middle_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Middle))
        element.click()
        return element

    def click_right_button(self):
        self.Navigation_page.go_to_buttons()
        element = self.wait.until(EC.presence_of_element_located(self.Right))
        element.click()
        return element