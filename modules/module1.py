import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_1:
    def test_method11(self,setup):
        assert True
    def test_method12(self,setup):
        assert True
    def test_login(self):
        driver=webdriver.Edge()
        driver.find_element_by_class_name()