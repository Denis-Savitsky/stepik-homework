from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    image = browser.find_element(By.TAG_NAME, 'img')
    x = int(image.get_attribute('valuex'))
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
    time.sleep(5)
