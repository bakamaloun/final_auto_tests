from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
#from .pages.locators import MainPageLocators
from selenium import webdriver
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.xfail # сообщение есть так ка добавили товар
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product() # добавили товар
    page.should_not_be_success_message() # проверяем что нет сообщения об успешно добавленном товаре

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message() # проверяем что нет сообщения об успешно добавленном товаре

@pytest.mark.xfail # сообщение не пропадает
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product() # добавили товар
    page.success_message_should_disappear() # проверяем что сообщение о добавленном товаре пропадает через 5 сек