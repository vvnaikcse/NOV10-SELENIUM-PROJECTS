from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge(executable_path="C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click() #lOGIN BUTTON
time.sleep(5)
driver.switch_to.alert.accept()

driver.close()