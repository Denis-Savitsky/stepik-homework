import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestElement(unittest.TestCase):
    def test_el_1(self):
        link = 'http://suninjuly.github.io/registration1.html'

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        first_name.send_keys('Ivan')

        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        last_name.send_keys('Ivanov')

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        email.send_keys('random_email@example.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Registration failed')
        browser.quit()

    def test_el_2(self):
        link = 'http://suninjuly.github.io/registration2.html'

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        first_name.send_keys('Ivan')

        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        last_name.send_keys('Ivanov')

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        email.send_keys('random_email@example.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Registration failed')
        browser.quit()

if __name__ == '__main__':
    unittest.main()

