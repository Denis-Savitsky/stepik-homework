from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.TAG_NAME, 'button')
    btn1.click()


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    print(new_window)

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