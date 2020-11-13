from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # press the button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # move to the new tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # ждем загрузки страницы
    time.sleep(1)

    # get x and calculate answer
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # set the answer
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # press the button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
