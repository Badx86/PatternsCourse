import os
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    browser = os.environ["BROWSER"]
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-search-engine-choice-screen")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-search-engine-choice-screen")
        driver = webdriver.Firefox(options=options)

    request.cls.driver = driver
    yield
    driver.quit()

