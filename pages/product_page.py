from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium import webdriver
import unittest
import time

class ProductPage(BasePage):

    def add_product(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_basket.click() # добавляем продукт

    def correct_price(self):
        # собираем информацию о продукте и корзине
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)

        #проверяем что информация совпадает
        assert book_name.text == added_book_name.text, \
            f"expected {book_name.text}, got {added_book_name.text}"

        assert book_price.text == total_price.text, \
            f"expected {book_price.text}, got {total_price.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"