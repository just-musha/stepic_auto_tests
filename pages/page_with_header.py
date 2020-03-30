from .base_page import BasePage
from .locators import PageWithHeaderLocators
from selenium import webdriver

class PageWithHeader(BasePage):
    def go_to_basket(self):
        assert self.is_element_present(*PageWithHeaderLocators.LINK_VIEW_BASKET), (
            "Basket link is not present on top of Main page")
        basket_link = self.browser.find_element(*PageWithHeaderLocators.LINK_VIEW_BASKET)
        basket_link.click()
