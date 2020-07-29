#coding:utf-8
from utils.operate_excel import operateExcel
from base.run_method import runMethod
from data.get_data import getData
from jsonpath_rw import parse
import json
class dependData:
    """
    通过case_id去获取case_id的整行数据
    """
    def __init__(self,case_id):
        self.case_id = case_id
        self.operate_excel =  operateExcel()
        self.get_data = getData()

    #根据case_id去获取对应case_id的数据
    def get_case_line_data(self):
        row_data = self.operate_excel.get_rows_data(self.case_id)
        return row_data

    #执行依赖测试，获取结果
    def run_depend(self):
        run_method = runMethod()
        row_num = self.operate_excel.get_row_num(self.case_id)
        request_data = self.get_data.get_data_for_json(row_num)
        header = self.get_data.is_header(row_num)
        method = self.get_data.get_method(row_num)
        url = self.get_data.get_request_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        return json.loads(res)

    #根据依赖的key获取依赖数据
    def get_data_for_key(self,row):
        depend_data = self.get_data.get_depend_key(row)
        respond_data = self.run_depend()
        json_exe = parse(depend_data)
        madle = json_exe.find(respond_data)
        return [math.value for math in madle][0]



