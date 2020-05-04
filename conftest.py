import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test.. with  ", language)
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()