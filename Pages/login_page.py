from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "This is not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "No email field"
        # email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        # email_field.send_keys(email)
        # assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), "No password1 field"
        # password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        # password1_field.send_keys(password)
        # assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), "No password2 field"
        # password2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        # password2_field.send_keys(password)
        self.send_keys_if_element_present(*LoginPageLocators.REGISTER_EMAIL, email, "email")
        self.send_keys_if_element_present(*LoginPageLocators.REGISTER_PASSWORD1, password, "password1")
        self.send_keys_if_element_present(*LoginPageLocators.REGISTER_PASSWORD2, password, "password2")

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        self.should_be_authorized_user()

