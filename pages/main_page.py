from .page_with_header import PageWithHeader
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(PageWithHeader):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
