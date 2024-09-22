from base.base_page import BasePage
from data.links import Links
from pages.contacts_page.components.filters import Filters


class ContactsPage(BasePage):

    _PAGE_URL = Links.CONTACTS_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = Filters(driver)
