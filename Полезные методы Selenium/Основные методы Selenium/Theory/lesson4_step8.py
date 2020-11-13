from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # wait until price = $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    # get x and calculate answer
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # set the answer
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # press the button
    button = browser.find_element_by_id("solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
