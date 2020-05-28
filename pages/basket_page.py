from .base_page import BasePage
from .locators import BasketPageLocators
from selenium import webdriver
import unittest
import time

class BasketPage(BasePage):

    def empty_basket_message_is_present(self):
        empty_text = "Your basket is empty." # ожидаемое сообщение о том что корзина пуста
        empty_basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY) # находим сообщение на странице
        # проверяем что тексты одинаковые
        assert empty_text in empty_basket_message.text, \
            f"expected {empty_text}, got {empty_basket_message.text}"

    def should_not_be_product_in_basket(self):
        # проверяем что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_ITEMS), \
            "Basket item is presented, but should not be"