import unittest
import Add_Products, Delete_Product,add_edit_shopping_cart_coupon,checkout
import SelectCatagory, add_edit_shopping_cart_coupon,create_account,login_logout
    

class ConfigTestCase(unittest.TestCase):
    
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')

def suite():
    
    test_suite = unittest.TestSuite()
   
    test_suite.addTest(unittest.loader.findTestCases(Add_Products))
    test_suite.addTest(unittest.loader.findTestCases(Delete_Product))
    test_suite.addTest(unittest.loader.findTestCases(add_edit_shopping_cart_coupon))
    test_suite.addTest(unittest.loader.findTestCases(checkout))
    test_suite.addTest(unittest.loader.findTestCases(SelectCatagory))
    test_suite.addTest(unittest.loader.findTestCases(add_edit_shopping_cart_coupon))
    test_suite.addTest(unittest.loader.findTestCases(create_account))
    test_suite.addTest(unittest.loader.findTestCases(login_logout))

    
    return test_suite

mySuit=suite()


runner=unittest.TextTestRunner()
runner.run(mySuit)