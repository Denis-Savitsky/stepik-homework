from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()

    browser.get(link)

    browser.implicitly_wait(5)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, 'price'), '$100'
    ))
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    result = math.log(abs(12 * math.sin(x)))

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(result))

    btn2 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
        (By.ID, 'solve')
    ))

    btn2.click()

    answer = browser.switch_to.alert.text.split()[-1]
    print(answer)
    pyperclip.copy(answer)

except Exception as ex:
    print(ex)

finally:
    browser.quit()



