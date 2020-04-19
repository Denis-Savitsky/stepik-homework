from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(2)').text

    operator = browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(3)').text

    second_number = browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(4)').text

    y = eval(first_number + operator + second_number)

    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(str(y))

    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    browser.quit()