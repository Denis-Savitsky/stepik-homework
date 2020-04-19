from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    for element in browser.find_elements(By.CSS_SELECTOR, ':required'):
        element.send_keys('aaaa')
        time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)

    