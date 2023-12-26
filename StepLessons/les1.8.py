import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/huge_form.html"
    browser.get(link)
    elems = browser.find_elements(By.CSS_SELECTOR, 'input')
    for el in elems:
        el.send_keys('Произвольно')

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(20)
finally:
    browser.quit()
