from selenium import webdriver
import time, os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Petrov')
    email = browser.find_element_by_name('email')
    email.send_keys('123@email.com')

    # filename
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_element = browser.find_element_by_name('file')
    file_element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
