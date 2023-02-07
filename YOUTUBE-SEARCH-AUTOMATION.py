from selenium import webdriver
#driver
driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
#get the youtube URL
driver.get("https://www.youtube.com")
driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("SPB")
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()
#facebook login automation
#instagram login automation
#amazon login automation
