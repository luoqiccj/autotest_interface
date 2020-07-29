#coding:utf-8
import psycopg2
from utils.get_config import getConfig
import utils.Log

log = utils.Log.logger

class operateDb:
    def __init__(self,dbsetion=None):
        if dbsetion == None:
            self.dbsetion = 'sit-database'
        else:
            self.dbsetion = dbsetion

        self.cfg = getConfig()

        db_name = self.cfg.get_config(self.dbsetion,'db_name')
        user = self.cfg.get_config(self.dbsetion, 'user')
        password = self.cfg.get_config(self.dbsetion, 'password')
        host = self.cfg.get_config(self.dbsetion, 'host')
        port = self.cfg.get_config(self.dbsetion, 'port')

        self.conn = psycopg2.connect(database=db_name, user=user, password=password, host=host,port=port)
        self.cur = self.conn.cursor()

    def operate_Db(self,sql):
        sql_name = sql
        self.cur.execute(sql_name)
        res = self.cur.fetchone()
        log.info("res = %s",res)
        log.info("self.dbsetion = %s",self.dbsetion)

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    sql = "select * from b_bas_company"
    operateDb().operate_Db(sql)
    operateDb("uat-database").operate_Db(sql)


