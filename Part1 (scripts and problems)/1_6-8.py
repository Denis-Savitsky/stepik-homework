from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
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
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)

    