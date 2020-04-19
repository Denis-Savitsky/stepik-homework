from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    print(x)
    result = math.log(abs(12 * math.sin(x)))

    browser.execute_script("window.scrollBy(0, 150);")

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(result))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

except Exception as ex:
   print(ex)

finally:
    browser.quit()

