#coding:utf-8
from base.run_method import runMethod
from data.get_data import getData
import json
from  utils.common_utils  import commonUtils
from data.depend_data import dependData
import utils.Log

log = utils.Log.logger

class runTest:
    def __init__(self,file_name=None):
        self.runmethod = runMethod()
        self.data = getData(file_name)
        log.info("file_name = %s",file_name)

    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_method(i)
                data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                expect_data  = self.data.get_except(i)
                depend_case_id = self.data.is_depent(i)

                if depend_case_id != None:
                    self.depend_data = dependData(depend_case_id)
                    depend_res = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_depend_field(i)
                    header[depend_key] = depend_res

                res = self.runmethod.run_main(method, url, data, header)

                result = commonUtils().is_contain(expect_data, res)
                if result:
                    self.data.write_result(i, "pass")
                else:
                    self.data.write_result(i, "fail")



if __name__ == '__main__':
    runTest("../dataconfig/queryCompanyByPage1.xlsx").go_on_run()
    runTest().go_on_run()

