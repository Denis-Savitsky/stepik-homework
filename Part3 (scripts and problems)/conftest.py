from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, etc.')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'Chrome':
        print("\nstart Chrome browser for test..")
        # language settings for Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        print("\nstart Firefox browser for test..")
        # language settings for Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f"--browser_name should be Chrome or Firefox, while your input is {browser_name}")

    yield browser
    print('\nquit browser...')
    browser.quit()