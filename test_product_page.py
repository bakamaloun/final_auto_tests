from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium import webdriver
import time
import pytest

# ссылки для теста test_guest_can_add_to_basket
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product() # добавляем продукт
    page.solve_quiz_and_get_code() # решаем задачу для получения кода
    page.correct_price() # проверка цены добавленного продукта

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page() # переходим в корзину с страницы товара
    page.should_not_be_product_in_basket() # проверяем что корзина пуста

@pytest.mark.need_review
@pytest.mark.xfail # используется невалидная ссылка
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page() # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # проверяем наличие логин формы

@pytest.mark.registration_guest
class TestUserAddToBasketFromProductPage():

    # регистрация нового пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "1234qwer!"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password) # создаем нового пользователя
        page.should_be_authorized_user() # проверяем что пользователь успешно создан

    # ссылки для теста test_user_can_add_to_basket
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    @pytest.mark.need_review
    def test_user_can_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product() # добавляем продукт
        page.solve_quiz_and_get_code() # решаем задачу для получения кода
        page.correct_price() # проверка цены добавленного продукта

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message() # проверяем что нет сообщения об успешно добавленном товаре