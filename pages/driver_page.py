from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser):
    if browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.add_argument("headless")
        return webdriver.Edge(service=service, options=options)
    elif browser == "chrome":
         service = ChromeService(ChromeDriverManager().install())
         options = webdriver.ChromeOptions()
         options.add_argument("headless")
         return webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
         service = FirefoxService(GeckoDriverManager().install())
         options = webdriver.FirefoxOptions()
         options.add_argument("headless")
         return webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported Driver")