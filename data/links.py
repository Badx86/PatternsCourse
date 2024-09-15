import os


# $env:STAGE="dev"; python data/links.py
class Links:
    HOST = f"https://{os.environ['STAGE']}-crm.qa-playground.com/#"

    CONTACTS_PAGE = f"{HOST}/contacts"
    COMPANIES_PAGE = f"{HOST}/companies"


print(Links.CONTACTS_PAGE)
print(Links.COMPANIES_PAGE)
