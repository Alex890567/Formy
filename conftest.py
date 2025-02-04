import pytest

from pages.autocomplete_page import AutocompletePage
from pages.driver_page import get_driver

from pages.navigation_page import NavigationPage


@pytest.fixture
def driver():
    # Modify the browser here if needed
    browser = "edge"
    driver = get_driver(browser)
    driver.get("https://formy-project.herokuapp.com/")
    yield driver
    driver.quit()


@pytest.fixture
def navigation_page(driver):
    return NavigationPage(driver)

@pytest.fixture
def autocomplete_page(driver, navigation_page):
    return AutocompletePage(driver, navigation_page)

