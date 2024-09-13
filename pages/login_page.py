from base.base_page import BasePage
import allure


class LoginPage(BasePage):
    _PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    _LOGIN_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"

    '''Декларативный интерфейс'''

    @allure.step("Login in account")
    def login(self, login, password):
        login_field = self.driver.find_element(*self._LOGIN_FIELD)
        password_filed = self.driver.find_element(*self._PASSWORD_FIELD)
        button = self.driver.find_element(*self._SUBMIT_BUTTON)
        login_field.send_keys(login)
        password_filed.send_keys(password)
        button.click()

    '''Императивный интерфейс'''

    @allure.step("Enter Login")
    def enter_login(self, login):
        login_field = self.driver.find_element(*self._LOGIN_FIELD)
        login_field.send_keys(login)

    @allure.step("Enter Password")
    def enter_password(self, password):
        password_filed = self.driver.find_element(*self._PASSWORD_FIELD)
        password_filed.send_keys(password)

    @allure.step("Click submit button")
    def login_button(self):
        button = self.driver.find_element(*self._SUBMIT_BUTTON)
        button.click()
