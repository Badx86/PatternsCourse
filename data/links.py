import os


class Links:
    HOST = f"https://{os.environ['STAGE']}-crm.qa-playground.com/#"

    CONTACTS_PAGE = f"{HOST}/contacts"
