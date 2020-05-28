from .base_page import BasePage
from .locators import LoginPageLocators
#from .locators import MainPageLocators
from .locators import BasePageLocators
from selenium import webdriver
import unittest
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        c_url = self.browser.current_url
        assert "login" in c_url, \
            f"expected Login page, got {c_url}"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), "Register email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "First register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Second register password is not presented"

    def register_new_user(self, email, password):
        # открываем форму регистрации
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        reg_login = self.browser.find_element(*LoginPageLocators.REG_MAIL)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        # заполняем форму
        reg_login.send_keys(email)
        reg_pass1.send_keys(password)
        reg_pass2.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        registration_btn.click() # регистрируем пользователя
