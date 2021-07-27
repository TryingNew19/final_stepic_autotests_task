from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default:nth-child(1)")
    # BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')

class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    #MAIN_BOOK_NAME = (By.CSS_SELECTOR, "a.dropdown-toggle")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    QUANTITY_FIELD = (By.CSS_SELECTOR, '[name="form-0-quantity"]')
    RENEW_BTN = (By.CSS_SELECTOR, '.input-group-btn > [type="submit"]')
    SEE_BASKET_BTN = (By.CSS_SELECTOR, '[href="/ru/basket/"].btn-info')


