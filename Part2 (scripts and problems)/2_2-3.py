from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys('Ivan')

    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys('Ivanov')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Ivan-bla-bla')

    upload = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    upload.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(1)

    message = browser.switch_to.alert.text
    print(message.split()[-1])



except Exception as ex:
    print(ex)

finally:
    browser.quit()