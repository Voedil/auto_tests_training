import os
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.find_element(By.CSS_SELECTOR, '.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    ans = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(ans)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(8)
except:
    browser.quit()