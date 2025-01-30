import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.navigation_page import NavigationPage


@pytest.fixture
def driver():
    # Set up the Edge WebDriver
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(service=service, options=options)
    driver.get("https://formy-project.herokuapp.com/")
    yield driver
    driver.quit()

@pytest.fixture
def navigation_page(driver):
    return NavigationPage(driver)

