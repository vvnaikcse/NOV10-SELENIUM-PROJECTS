from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
#driver.find_element_by_xpath("//button[normalize-space()='Click for JS Alert']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("welcome")


#alertwindow.accept() #close alert window by using OK button
alertwindow.dismiss() #close alert window by using Cancel button