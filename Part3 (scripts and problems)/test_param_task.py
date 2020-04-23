from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
import math

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('link', links)
class TestParams():

    def test_parametrization(self, browser,link):
        browser.get(link)
        textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'textarea'))
        )
        textarea.send_keys(str(math.log(int(time.time()))))
        button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        button.click()
        respond = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        ).text
        assert respond == 'Correct!'

