from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")
print("Opened site")
time.sleep(2)
driver.quit()