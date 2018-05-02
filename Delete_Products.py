import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime


#
class Test_addProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_user_login(self):
        user = "instructor"  # instructor
        pwd = "instructor1a"  # instructor1a
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        # driver.get("http://127.0.0.1:8000/login") -
        driver.find_element_by_xpath('//*[@id="main"]/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        driver.find_element_by_xpath('//*[@id="main"]/div[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
