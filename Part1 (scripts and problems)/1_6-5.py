from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'
value = 'input'

with webdriver.Chrome() as browser:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, value)
    for element in elements:
        element.send_keys('Мой ответ')
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(30)

