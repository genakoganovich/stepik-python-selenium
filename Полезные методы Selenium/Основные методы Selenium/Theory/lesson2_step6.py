from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # scroll
    form_to_scroll = browser.find_element_by_css_selector('form[method="get"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", form_to_scroll)

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()
    robot_radio_button = browser.find_element_by_id('robotsRule')
    robot_radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
