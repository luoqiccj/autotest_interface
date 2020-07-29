import os
import unittest
from utils.operate_excel import operateExcel
from data.get_data import getData
import utils.Log
import base.HTMLTestRunner as HTMLTestRunner
from utils.send_email import sendEmail
from utils.get_config import getConfig

import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print("rootPath",rootPath)

log = utils.Log.logger
on_off = getConfig().get_config("email","on_off")
usr_list = getConfig().get_config("email","recv_usr_list")
sub = getConfig().get_config("email","sub")
content = getConfig().get_config("email","content")


class AllTest:
    def __init__(self):
        global resultPath
        resutldir = os.path.dirname(os.getcwd())
        resultPath = os.path.join(resutldir,'testReport',"report.html")
        self.caseListFile = os.path.join(resutldir,'testcase',"caselist.txt")
        self.caseFile = os.path.join(resutldir,'testcase')
        self.caseList = []
        log.info('resultPath=%s', resultPath)

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suite(self):
        """
        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            log.info("case_name = %s",case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组

        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
                    log.info("test_name = %s",test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            log.info(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                fp = open(resultPath, 'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            log.info("*********TEST END*********")
            # log.info("*********TEST END*********")
            fp.close()
        # 判断邮件发送的开关
        if on_off == 'on':
            sendEmail().send_email2(usr_list,sub,content)
        else:
            log.info("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()

if __name__ == '__main__':
    AllTest().run()