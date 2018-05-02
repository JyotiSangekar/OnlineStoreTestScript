import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Checkout_Form(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_fill_out_and_submit_checkout_form(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/orders/create/')
        print('Checkout Form is available to fill-out')
        time.sleep(2)

        name = self.driver.find_element_by_name('first_name')
        name.send_keys('Jyoti')
        time.sleep(2)

        last_name = self.driver.find_element_by_name('last_name')
        last_name.send_keys('XYZ')
        time.sleep(2)

        email = self.driver.find_element_by_name('email')
        email.send_keys('jyotixyz@gmail.com')
        time.sleep(2)

        address = self.driver.find_element_by_name('address')
        address.send_keys('444 S,72nd street')
        time.sleep(2)

        zipcode = self.driver.find_element_by_name('postal_code')
        zipcode.send_keys('68106')
        time.sleep(2)

        city_name = self.driver.find_element_by_name('city')
        city_name.send_keys('Omaha')
        time.sleep(2)

        submit_order = self.driver.find_element_by_id('submit_order')
        submit_order.click()
        time.sleep(2)

        print('Successfully filled-out Checkout Form')

    def tearDown(self):
        self.driver.quit()


    if __name__ == "__main__":
        unittest.main()

