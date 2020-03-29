from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_correct_product_name()
    page.should_be_message_added_to_basket()
    page.should_be_same_price_product_and_bucket()
    pass
