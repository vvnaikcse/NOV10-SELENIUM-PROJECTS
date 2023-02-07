import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

#locate elements in facebook login page with name locator
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("career.nthss@gmail.com")
driver.find_element_by_id("pass").send_keys("Srini@143")
driver.find_element_by_name("login").click()
time.sleep(5)
driver.close()
