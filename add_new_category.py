import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_page (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

#add category as admin
    def test_add_catgory(self):
        driver = self.driver
        driver.maximize_window()
        driver.get ("http://127.0.0.1:8000/admin/login/")
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys('wsun')
        time.sleep(2)
        elem = driver.find_element_by_id ("id_password")
        elem.send_keys('Kee177Cay')
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/admin/shop/category/add/")
        elem = driver.find_element_by_id ("id_name")
        elem.send_keys('Clothes')
        time.sleep(2)
        elem = driver.find_element_by_id("id_slug")
        elem.send_keys('cloth')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="category_form"]/div/div/input[1]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
