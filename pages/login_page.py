from base.base_page import BasePage
from data.links import Links


class LoginPage(BasePage):
    _PAGE_URL = Links.LOGIN_PAGE

    _USERNAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"

    def login_as(self, login, password):
        self.driver.find_element(*self._USERNAME_FIELD).send_keys(login)
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self._SUBMIT_BUTTON).click()
