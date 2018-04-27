import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Select_Categories(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_select_and_check_diff_categories(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000')
        print ('Shopping site is available for shop')
        time.sleep(2)

        # Shows products in All categories
        select_all = self.driver.find_element_by_link_text('All')
        select_all.click()
        time.sleep(2)

        # Shows products in Beauty category products
        select_cat_Beauty= driver.find_element_by_link_text('Beauty')
        select_cat_Beauty.click()
        time.sleep(2)

        # Shows products in Clothing & Accessories category products
        category3= driver.find_element_by_link_text('Clothing & Accessories')
        category3.click()
        time.sleep(3)

        # Shows products in Grocery category products
        category4= driver.find_element_by_link_text('Grocery')
        category4.click()
        time.sleep(3)

        # Shows products in Health category products
        category5 = driver.find_element_by_link_text('Health')
        category5.click()
        time.sleep(3)

        # Shows products in Books category products
        category6 = driver.find_element_by_link_text('Books')
        category6.click()
        time.sleep(3)

        print('Successfully shown ALL the Categories from shopping site')

    def tearDown(self):
        self.driver.quit()


    if __name__ == "__main__":
        unittest.main()