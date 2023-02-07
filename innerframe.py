from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge(executable_path="C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

#driver.switch_to.parent_frame()  # directly switch to parent frame(outerframe)
