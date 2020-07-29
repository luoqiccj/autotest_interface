#coding:utf-8
import json
class commonUtils:
    def is_contain(self,str_one,str_two):
        flage = None
        str_two = json.dumps(str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

if __name__ == '__main__':
    res = commonUtils().is_contain("1","12")
    print(res)
