from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.chrome.webdriver import WebDriver
from data.credentials import Credentials
import allure


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.credentials = Credentials()

    def open(self):
        with allure.step(f"Open page: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

