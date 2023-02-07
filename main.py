#WRITE A PYTHON SCRIPT USING SELENIUM WEBDRIVER
#TO CHECK GOOGLE SEARCH ENGINE WORKING PROPERLY OR NOT
from selenium import webdriver
#setup chrome driver to be loaded
driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
#load desired web application to test
driver.get("https://www.google.com")
#code to locate textbox in the google search engine where keywords are provided
driver.find_element_by_name(name="q").send_keys("midde venkateswarlu naik")
# code to click on to the google search button
#driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[2]/button").click()
#driver.find_element_by_name(name="btnK").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
