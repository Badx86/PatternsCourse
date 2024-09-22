import time
from base.base_test import BaseTest


class TestContacts(BaseTest):

    def test_example(self):
        self.contacts_page.open()
        time.sleep(3)
        self.contacts_page.filters.click_today_filter()
        time.sleep(3)
