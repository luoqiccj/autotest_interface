import  json
import unittest
from main.run_test import runTest
from data.get_data import getData
from utils.operate_db import operateDb

class test_queryCompanyByPage(unittest.TestCase):
    def setUp(self):
        self.run_test = runTest()
        self.db = operateDb()
        self.db1 = operateDb("uat-database")

        sql = "select * from b_bas_company"
        self.db.operate_Db(sql)
        self.db1.operate_Db(sql)

    def tearDown(self):
        pass

    def testcase01(self):
        self.run_test.go_on_run()

    def testcase02(self):
        self.run_test.go_on_run()





