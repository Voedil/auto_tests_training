import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://101.stage.tanto-s.ru/#/events")
time.sleep(5)

login = driver.find_element(By.CSS_SELECTOR, "input[name='login']")
login.send_keys('sys112')
time.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.send_keys('Qwerty1234@@')
time.sleep(2)
signIn = driver.find_element(By.CSS_SELECTOR, "button.signInBtn")
signIn.click()
time.sleep(6)

dalee = driver.find_element(By.CSS_SELECTOR, "button#btn_selectDesk")
dalee.click()
time.sleep(5)
monitoring = driver.find_element(By.CSS_SELECTOR, "button#btn_statistics")
monitoring.click()
time.sleep(2)
monitoring.click()
time.sleep(3)
map = driver.find_element(By.CSS_SELECTOR, "button#btn_searchAsMap")
map2 = driver.find_element(By.CSS_SELECTOR, "button#btn_searchAsTable")
map.click()
time.sleep(3)
map2.click()
time.sleep(4)
21.254931787059697
# textarea.send_keys("get()")
# time.sleep(5)
#
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
#
# submit_button.click()
# time.sleep(5)
#
# driver.quit()