from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def shoul_be_added_thing_in_basket(self):
        self.add_to_basket()
        self.should_be_thing_in_basket()
        self.should_be_same_price()

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        button_add_to_basket.click()

    def should_be_thing_in_basket(self):
        main_book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        assert main_book_name.text == alert_book_name.text, "book name is {}, but alert book name is {}".format(main_book_name.text, alert_book_name.text)

    def should_be_same_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert basket_price.text == book_price.text, "basket prise is {}, but book price is {}".format(basket_price.text, book_price.text)

#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         login_link.click()
#         # variant1
#         # return LoginPage(browser=self.browser, url=self.browser.current_url)
#
# def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
