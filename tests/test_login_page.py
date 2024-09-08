import time
import allure
import pytest
from base.base_test import BaseTest


@allure.epic("Users")
@allure.feature("Trial Accounts")
@allure.story("New Accounts")
class TestLoginPage(BaseTest):

    @allure.title("LogIn in new trial account")
    def test_login_in_account(self):
        self.login_page.open()
        time.sleep(3)
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.login_button()
        time.sleep(1)
        self.dashboard_page.click_help()
        time.sleep(3)
