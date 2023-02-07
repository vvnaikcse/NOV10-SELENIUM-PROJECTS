
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
#driver.get("https://demo.nopcommerce.com/")
#driver.get("https://nthlearnings.com/")
driver.get("https://www.amazon.in/")
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.LINK_TEXT,"Signup").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
sliders=driver.find_elements(By.CLASS_NAME,"a-")
time.sleep(10)
