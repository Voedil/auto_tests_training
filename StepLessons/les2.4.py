import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
# browser.implicitly_wait(5)
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'solve').click()
    time.sleep(6)


finally:
    browser.quit()