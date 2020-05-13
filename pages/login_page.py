from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium import webdriver
import unittest
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        c_url = self.browser.current_url
        assert "login" in c_url, \
            f"expected Login page, got {c_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), "Register email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "First register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Second register password is not presented"
