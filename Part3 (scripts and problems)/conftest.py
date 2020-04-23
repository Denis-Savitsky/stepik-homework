from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: Chrome or Firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'Chrome':
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'Firefox':
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"--browser_name should be Chrome or Firefox, while your input is {browser_name}")
    yield browser
    print('\nquit browser...')
    browser.quit()