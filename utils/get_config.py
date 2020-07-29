#coding:utf-8
import sys
sys.path.append("C:/Users/luoqi/PycharmProjects/Interface3")
from configparser import ConfigParser
import os

class getConfig:

    def get_project_path(self):
        pro_path = os.path.abspath(os.path.dirname(os.getcwd()))
        return pro_path

    def get_cfg_path(self):
        cfg_path = os.path.join(self.get_project_path(),"config","config.ini")
        return cfg_path

    def get_config(self,setion,option,file_name=None):
        cfg = ConfigParser()
        if file_name == None:
            file_name = self.get_cfg_path()

        cfg.read(file_name,encoding='utf-8')
        value = cfg.get(setion,option)
        return value

if __name__ == '__main__':
   cfg =  getConfig()
   print(cfg.get_config('email','email_host'))



