import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    inp1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    inp1.send_keys('Max')
    inp2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    inp2.send_keys('Huyax')
    inp3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    inp3.send_keys('biba@ya.ru')
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(2)

    welcome_page = browser.find_element(By.TAG_NAME, 'h1')
    welcome = welcome_page.text

    assert welcome == 'Congratulations! You have successfully registered!'


finally:
    browser.quit()
