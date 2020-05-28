from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from selenium import webdriver
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.xfail # используется невалидная ссылка
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page() # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page() # проверяем наличие логин формы

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link() # проверяем наличие ссылки на страницу логина

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page() # проверяем наличие логин формы

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page() # открываем корзину
    page.empty_basket_message_is_present() # проверяем что корзина пуста

