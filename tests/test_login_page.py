import time
from base.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_login_in_account(self):

        self.login_page.open()
        time.sleep(3)
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        time.sleep(3)
        self.login_page.login_button()
        self.dashboard_page.click_help()
        time.sleep(3)

