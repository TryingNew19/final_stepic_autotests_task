from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Busket items are presented, but should not be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
        "Should be text about empty basket"