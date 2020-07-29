#coding:utf-8

import json

class operateJson():
    def __init__(self,file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../dataconfig/param.json"

        self.data = self.get_json()

    def get_json(self):
        with open(self.file_name) as fp:
            data = json.load(fp)
        return data

    def get_data(self,id):
        return json.dumps(self.data[id])

if __name__ == '__main__':
    data = operateJson().get_data("login")
    print(data)

