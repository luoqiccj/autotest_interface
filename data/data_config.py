#coding:utf-8

class global_var:
    Id = '0'
    case_name = '1'
    url = '2'
    run ='3'
    method ='4'
    header = '5'
    depend_id = '6'
    depend_data = '7'
    depend_field = '8'
    data = '9'
    expect = '10'
    real_res = '11'

def get_id():
    return global_var.Id

def get_case_name():
    return global_var.case_name

def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_method():
    return global_var.method

def get_header():
    return global_var.header

def get_depend_id():
    return global_var.depend_id

def get_depend_data():
    return global_var.depend_data

def get_depend_field():
    return global_var.depend_field

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_real_res():
    return global_var.real_res


if __name__ == '__main__':
    print(get_id())
    print(get_except())
