import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'label')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    ans = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(ans)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()


    time.sleep(10)
finally:
    browser.quit()