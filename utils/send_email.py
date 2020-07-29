#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.get_config import getConfig
import os
import base64
import utils.Log

log = utils.Log.logger

class sendEmail:
    def __init__(self):
        self.cfg = getConfig()

    def send_email(self,usr_list,sub,context):
        user = self.cfg.get_config("email","sender")
        message = MIMEText(context,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(usr_list)

        server = smtplib.SMTP()
        email_host =  self.cfg.get_config("email","email_host")

        server.connect(email_host)
        password = self.cfg.get_config("email", "password")
        server.login(user,password)
        server.sendmail(user,usr_list,message.as_string())
        server.close()

    def send_email2(self,usr_list,sub,context):
        user = self.cfg.get_config("email","sender")
        file = "C:/Users/luoqi/PycharmProjects/Interface3/testReport/report.html"

        msg = MIMEMultipart()
        if file:  # 处理附件的
            file_name = os.path.split(file)[-1]  # 只取文件名，不取路径
            log.info("file_name = %s",file_name)
            try:
                f = open(file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(context))  # 邮件正文的内容
        msg['Subject'] = sub  # 邮件主题
        msg['From'] = user  # 发送者账号
        msg['To'] =  usr_list  # 接收者账号列表
        log.info("usr_list = %s",usr_list)
        log.info("msg['To']  = %s",msg['To'] )
        email_host = self.cfg.get_config("email", "email_host")
        log.info("email_host = %s",email_host)
        server = smtplib.SMTP()
        server.connect(email_host)
        # 发送邮件服务器的对象
        password = self.cfg.get_config("email", "password")
        server.login(user, password)
        try:
            server.sendmail(user, str(usr_list).split(","), msg.as_string())
            pass
        except Exception as e:
            log.info('出错了。。', e)
        else:
            log.info('邮件发送成功！')
        server.close()


if __name__ == '__main__':
    send = sendEmail()
    cfg = getConfig()
    usr_list =cfg.get_config("email","recv_usr_list")
    sub=cfg.get_config("email","sub")
    context = "接口测试报告"
    #send.send_email(usr_list, sub, context)
    send.send_email2(usr_list,sub,context)

