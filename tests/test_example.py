import time
import allure
import pytest
from base.base_test import BaseTest


class TestExample(BaseTest):
    #  $env:STAGE="{dev/release}"; pytest -sv
    # $env:STAGE="release"; $env:BROWSER="chrome"; python -sv
    def test_example(self):
        self.contacts_page.open()
        time.sleep(3)
        self.comapnies_page.open()
        time.sleep(3)
