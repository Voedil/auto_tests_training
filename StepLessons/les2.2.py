import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys('Max')
    browser.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys('Voedilov')
    browser.find_element(By.CSS_SELECTOR, '[name=email]').send_keys('maxvoedil@gmail.com')
    dirr = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(dirr, 'text.txt')
    inp = browser.find_element(By.ID, 'file')
    inp.send_keys(file)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(7)
except:
    browser.quit()