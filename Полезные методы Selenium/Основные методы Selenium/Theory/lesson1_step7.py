from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name('img')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)
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
