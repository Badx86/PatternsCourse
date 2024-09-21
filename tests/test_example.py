import time
import allure
import pytest
from base.base_test import BaseTest


class TestExample(BaseTest):

    def test_example(self):
        admin = self.browser_factory()
        manager = self.browser_factory()

        self.login_page().open()
        self.login_page().login_as(self.credentials.LOGIN, self.credentials.PASSWORD)

        self.login_page(admin).open()
        self.login_page().click()
