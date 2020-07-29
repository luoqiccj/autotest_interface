#coding:utf-8

from  utils.operate_excel import operateExcel
import  data.data_config as data_config
from utils.operate_json import  operateJson
import json

class getData:
    def __init__(self,file_name=None):
        self.operate_excel = operateExcel(file_name)

    #获取用例行数
    def get_case_lines(self):
        return self.operate_excel.get_lines()

    #获取用例是否执行字段的值
    def is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_method = self.operate_excel.get_cell_value(row,col)
        if run_method == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取用例的header值
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.operate_excel.get_cell_value(row, col)
        if header =='':
           return  None
        return  json.loads(header,strict=False)

    # 获取请求方式
    def get_method(self,row):
        col = int(data_config.get_method())
        method = self.operate_excel.get_cell_value(row, col)
        return method
    #   获取请求url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        url = self.operate_excel.get_cell_value(row, col)
        return url

    #   获取请求参数
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.operate_excel.get_cell_value(row, col)
        if data == '':
            return  None
        return data

    #   获取预期结果
    def get_except(self,row):
        col = int(data_config.get_expect())
        expect = self.operate_excel.get_cell_value(row, col)
        return expect

    #   获取实际结果
    def get_result(self, row):
        col = int(data_config.get_real_res())
        result = self.operate_excel.get_cell_value(row, col)
        return result

    #通过关键字获取json参数
    def get_data_for_json(self,row):
        opera_json = operateJson()
        data = opera_json.get_data(self.get_request_data(row))
        return data

    def write_result(self,row,value):
        col = int(data_config.get_real_res())
        self.operate_excel.write_value(row,col,value)

    def get_depend_key(self,row):
        col = int(data_config.get_depend_data())
        depend_key = self.operate_excel.get_cell_value(row, col)
        return depend_key

    def is_depent(self,row):
        col = int(data_config.get_depend_id())
        depend_id = self.operate_excel.get_cell_value(row, col)
        if depend_id == '':
            return None
        else:
            return depend_id
    def get_depend_field(self,row):
        col = int(data_config.get_depend_field())
        result = self.operate_excel.get_cell_value(row, col)
        return result



if __name__ == '__main__':
    print("flag = ",getData("queryCompanyByPage1.xlsx").is_run(1))
    print(getData().get_data_for_json(1))



