import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class shopping_cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

#login
    def test_Login(self):
        driver = self.driver
        driver.get("https://shopmyown.herokuapp.com/")
        time.sleep(4)
        elem = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').click()
        time.sleep(4)
        id_login = "wsun"
        elem = driver.find_element_by_id("id_login")
        elem.send_keys(id_login)
        id_password = "123"
        elem = driver.find_element_by_id("id_password")
        time.sleep(4)
        elem = driver.find_element_by_xpath('/html/body/form/button').click()
        time.sleep(4)

#logout
        elem = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').click()

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()