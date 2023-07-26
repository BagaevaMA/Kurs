from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import timespan
import time


driver = webdriver.Chrome()

driver.get('https://passport.yandex.ru/auth/')

input_email = driver.find_element(by=By.ID, value='passp-field-login')
input_email.send_keys("test@test.ru")

time.sleep(2)

click_btn_log_in = driver.find_element(by=By.XPATH, value= '//*[@id="passp:sign-in"]')
click_btn_log_in.click()

time.sleep(2)

input_password = driver.find_elements(by=By.ID, value='passp-field-passwd')
input_password[0].send_keys("1234567")

time.sleep(2)

click_btn_log_in = driver.find_element(by=By.ID, value='passp:sign-in')
click_btn_log_in.click()

driver.close()
