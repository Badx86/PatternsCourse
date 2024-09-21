from data.credentials import Credentials
from pages.login_page import LoginPage
from selenium import webdriver
import os


class BaseTest:

    def setup_method(self):
        self.drivers = []
        self.default_user = self.browser_factory()
        self.credentials = Credentials()
        self.login_page = lambda driver=self.default_user: LoginPage(driver)

    def browser_factory(self):

        browser = os.environ["BROWSER"]

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-search-engine-choice-screen")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--disable-search-engine-choice-screen")
            driver = webdriver.Firefox(options=options)

        self.drivers.append(driver)

        return driver

    def teardown_method(self):
        for driver in self.drivers:
            if driver:
                driver.quit()

