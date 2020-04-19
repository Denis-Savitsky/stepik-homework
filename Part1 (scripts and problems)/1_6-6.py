from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"
value1 = 'input'
value2 = 'last_name'
value3 = 'form-control.city'
value4 = 'country'
value_button = r"//button[text()='Submit']"


with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME,  value1)
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.NAME,  value2)
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CLASS_NAME,  value3)
    input3.send_keys('Smolensk')
    input4 = browser.find_element(By.ID,  value4)
    input4.send_keys('Russia')
    button = browser.find_element(By.XPATH, value_button)
    button.click()

    time.sleep(30)