from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Edge(executable_path="C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
#driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()