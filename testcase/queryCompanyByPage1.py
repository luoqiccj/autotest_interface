import  json
import unittest
from main.run_test import runTest
from data.get_data import getData

class test_queryCompanyByPage(unittest.TestCase):
    def setUp(self):
        self.run_test = runTest("../dataconfig/queryCompanyByPage1.xlsx")

    def tearDown(self):
        pass

    def testcase01(self):
        self.run_test.go_on_run()

    def testcase02(self):
        self.run_test.go_on_run()






