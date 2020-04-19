from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import math

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.TAG_NAME, 'button')
    btn1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    result = math.log(abs(12 * math.sin(x)))

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(result))

    btn2 = browser.find_element(By.TAG_NAME, 'button')
    btn2.click()

    answer = browser.switch_to.alert.text.split()[-1]
    print(answer)
    pyperclip.copy(answer)

except Exception as ex:
    print(ex)

finally:
    browser.quit()