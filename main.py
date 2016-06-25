import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'http://adf.ly/1ZxAQX'
print("url =",url)
print("loading")
driver = webdriver.PhantomJS('phantomjs')
print("connecting")
driver.get(url)
print("connected")
wait = WebDriverWait(driver, 10)
print("waiting")
element = wait.until(EC.element_to_be_clickable((By.ID,"skip_button")))
print("clicking")
element.click()
print(driver.current_url)
driver.quit()
