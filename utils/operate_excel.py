#coding:utf8

import xlrd
from xlutils.copy import copy

class operateExcel():
    def __init__(self,file_name=None,sheet_id=None):
        if file_name != None:
            self.file_name = "../dataconfig/"+ file_name
        else:
            self.file_name = "../dataconfig/queryCompanyByPage.xlsx"

        if sheet_id !=None:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0
        self.data = self.get_data()

    #获取excel内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    #获取行数
    def get_lines(self):
        table = self.data
        return  table.nrows

    #获取单元格内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入测试结果
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据case_id找到对应行
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    #根据case_id找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_value()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num+1

    #根据行号，找到行的内容
    def get_row_value(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取列的数据
    def get_cols_value(self,col=None):
        tables = self.data
        if col != None:
            cols_data = tables.col_values(col)
        else:
            cols_data = tables.col_values(0)
        return cols_data

if __name__ == '__main__':
    print(operateExcel().get_cell_value(1,1))