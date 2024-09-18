from pages.contacts_page import ContactsPage
from pages.companies_page import CompaniesPage
from data.credentials import Credentials


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
