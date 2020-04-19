from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(int(x))

    y_element = browser.find_element(By.CLASS_NAME, 'form-control')
    y_element.send_keys(y)

    robot = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robot.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robots_rule.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

    time.sleep(10)


