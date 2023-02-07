import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()
driver.get("https://facebook.com")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("career.nthss@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("Srini@143")
#driver.find_element(By.CSS_SELECTOR,"button#login").click()
time.sleep(10)