import time
import pytest
from selenium import webdriver
class Test_class:
    def test_method1():
        name="nth"
        assert name=="nth", "FAILED"
    def test_method2():
        number=200
        assert number==200,"test method2 failed"
    def test_google_search():
        driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").send_keys("spb")
        driver.find_element_by_name("btnK").click()
        time.sleep(10)
    def test_facebook_login():
        pass

    def test_instagram_login():
        pass
