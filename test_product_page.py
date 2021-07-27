from .Pages.product_page import ProductPage
import pytest
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize('param_link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, param_link):
    # link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, param_link)
    page.open()  # открываем страницу
    page.add_to_basket() #добавляем товар в корзину
    page.solve_quiz_and_get_code() #вычисляем выражение и записываем его в алерт
    page.should_be_thing_in_basket(page.return_book_name())
    page.should_be_same_price(page.return_book_price())

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket()  # добавляем товар в корзину
    page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket()  # добавляем товар в корзину
    page.should_disappear_message() #Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.debug
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_open_basket()  # Переходит в корзину по кнопке в шапке сайта
    basket_link = browser.current_url
    basket_page = BasketPage(browser, basket_link)
    basket_page.should_not_be_goods_in_basket() #Ожидаем, что в корзине нет товаро

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, request):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        email = self.page.make_random_email()
        password = self.page.make_random_str(10)
        self.page.register_new_user(email, password)

        # для тренировки в teardown перейду в корзину и очищу корзину (удалю книгу)
        def teardown():
            page = ProductPage(browser, browser.current_url)
            page.open()  # открываем страницу
            page.should_open_basket() #открываем корзину
            basket_page = BasketPage(browser, browser.current_url)
            basket_page.delete_book() #удаляем книгу из корзины и проверяем, что она удалена

        request.addfinalizer(teardown)


    # def test_user_cant_see_success_message(self, browser):
    #     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    #     page = ProductPage(browser, link)
    #     page.open()  # открываем страницу
    #     page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6'
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.add_to_basket() #добавляем товар в корзину
        page.solve_quiz_and_get_code() #вычисляем выражение и записываем его в алерт
        page.should_be_thing_in_basket(page.return_book_name())
        page.should_be_same_price(page.return_book_price())




    #запуск pytest - s test_product_page.py
