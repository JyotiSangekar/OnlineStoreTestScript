import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class shopping_cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_account(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://shopmyown.herokuapp.com/accounts/signup/")
        time.sleep(4)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("customer1")
        time.sleep(4)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("customer1@gmail.com")
        time.sleep(4)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("123456")
        time.sleep(4)
        elem = driver.find_element_by_id("id_password2")
        time.sleep(4)
        elem = driver.find_element_by_xpath('//*[@id="signup_form"]/button').click()

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()