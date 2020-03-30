from .base_page import BasePage
from .locators import LoginPageLocators

from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on page"

    def register_new_user(self, email, password):
        inp_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        inp_email.send_keys(email)

        inp_passwd1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        inp_passwd2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONF)
        inp_passwd1.send_keys(password)
        inp_passwd2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT_REGISTER)
        button.click()
