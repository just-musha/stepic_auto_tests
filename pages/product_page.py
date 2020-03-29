from .locators import ProductPageLocators
from .base_page import BasePage
import time

class ProductPage(BasePage):
    def press_button_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not present")

        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET), (
            "Message about product added to basket is not present")

        msg = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET).text
        assert "has been added to your basket" in msg, "Incorrect text in message"

    def should_be_correct_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), (
            "Product is not present on page")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not present on page")
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        print(f"===== product_in_basket={product_in_basket} and product_name={product_name}")
        assert product_name == product_in_basket, f"Product in basket ({product_in_basket}) is not '{product_name}'"

    def should_be_same_price_product_and_bucket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), (
            "Basket price is not present on page")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not present on page")

        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert product_price in basket_total, "Busket total is not equal to product price"
