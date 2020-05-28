from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK_OLD = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_MAIL = (By.CSS_SELECTOR, "#id_login-username") # поле для ввода почты логина
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password") # поле пароля для логина
    REG_MAIL = (By.CSS_SELECTOR, "#id_registration-email") # поле почты для регистрации
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1") # поле первого пароля для регистраци
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2") # поле второго пароля для регистрации
    REG_BTN = (By.CSS_SELECTOR, "div.col-sm-6.register_form .btn.btn-lg.btn-primary") # кнопка зарегистрировать пользователя

class ProductPageLocators():
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']") # цена книги
    BOOK_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1") # название книги
    ADDED_BOOK_NAME = (By.XPATH, "//div[@id='messages']/div[1]//strong") # название добавленной книги
    TOTAL_PRICE = (By.XPATH, "//div[@id='messages']/div[3]//strong") # цена всех добавленных товаров
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//div") # сообщение об успешно добавленном товаре
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket") #кнопка добавить товар

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # переход на страницу логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") # некорректная ссылка на страницу логина для нег тестов
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a.btn.btn-default") # страница корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # иконка юзера

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p") # сообщение о том что корзина пуста
    BASKET_HAS_ITEMS = (By.XPATH, "//div[@class='col-sm-4']//a")  #сообщение о том что в кгорзине есть товары