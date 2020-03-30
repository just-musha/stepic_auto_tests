from .page_with_header import PageWithHeader
from .locators import BasketPageLocators, PageWithHeaderLocators

class BasketPage(PageWithHeader):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), (
            "Message is not present on basket page")
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "basket is empty" in msg, f"Unexpected message: {msg}"

    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Unexpected items in basket"
