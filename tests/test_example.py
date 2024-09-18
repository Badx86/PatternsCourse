import time
import allure
import pytest
from base.base_test import BaseTest


class TestExample(BaseTest):

    def test_example(self):
        self.login_page.open()
        time.sleep(3)
        self.login_page.login_as(self.credentials.LOGIN, self.credentials.PASSWORD)
        time.sleep(4)
