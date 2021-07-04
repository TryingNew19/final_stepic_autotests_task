from .Pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket() #добавляем товар в корзину
    page.solve_quiz_and_get_code() #вычисляем выражение и записываем его в алерт
    page.should_be_thing_in_basket(page.return_book_name())
    page.should_be_same_price(page.return_book_price())

    #запуск pytest - s test_product_page.py
