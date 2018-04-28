import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.support.ui import Select

class shopping_cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()



    def test_add_edit_shopping_cart(self):
        user = "admin"
        pwd = "nollywood"
        driver = self.driver
        driver.maxmize_window()
        driver.get ("http://127.0.0.1:8000/")
        time.sleep(2)


#add item to shopping cart
        elem = driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(2)

        assert "add item to shopping cart"

#edit quantity in shopping cart
        select = Select(driver.find_element_by_name ("quantity"))
        select.select_by_value('7')
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[3]/form/input[2]').click()
        time.sleep(2)

        assert "add item and edit quantity to shopping cart"

#apply coupon in shopping cart
        elem = driver.find_element_by_id ("id_code")
        elem.send_keys('christmas1225')
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="content"]/form/input[2]').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="content"]/p[2]/a[1]').click()
        time.sleep(2)

        assert  "apply coupon and shop again"


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

