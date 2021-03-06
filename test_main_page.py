from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage
import pytest

# запуск pytest -v --tb=line --language=en test_main_page.py
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_login_url()

# variant1
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()

@pytest.mark.login_guest
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open() #Гость открывает главную страницу
    page.should_open_basket() #Переходит в корзину по кнопке в шапке сайта
    basket_link = browser.current_url
    basket_page = BasketPage(browser, basket_link)
    basket_page.should_not_be_goods_in_basket() #Ожидаем, что в корзине нет товаров



#https://stepik.org/lesson/193188/step/4?unit=167629 урок про requirements


