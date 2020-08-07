#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/14 10:17
# @Author  : Fold
import pymysql
from common.config_log import log
from config.read_config import rc


class ExecuteSql():

    def __init__(self):
        self.host = rc.get_db("host")
        self.port = rc.get_db("port")
        self.user = rc.get_db("user")
        self.password = rc.get_db("password")

    def open(self):
        """
        连接数据库
        :param environment: 数据库环境链接
        :return:
        """
        # 连接数据库,
        self.conn = pymysql.connect(host=  self.host, user= self.user, password= self.password, port=3306)
        # 创建游标
        self.cur = self.conn.cursor()

    #数据库关闭方法:
    def close(self):
        self.conn.close()

    #数据库查询所有操作方法:
    def query(self, sql):
        """
        查询并返回一个结果
        :param sql:
        :param environment:
        :return:
        """
        self.open()
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            desc = self.cur.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
            data = [dict(zip([col[0] for col in desc], row)) for row in result]  # 列表表达式把数据组装起来
            # #拿到第一条数据
            # rs = result[0]
            # #将数组转换成string
            # data = ",".join(map(str, rs))
            # # print(data)
            return data
        except Exception as e:
            print("Failed", e)
        self.cur.close()


    def exec_sql(self, sql):
        """
        执行sql语句（update,delete,add）
        :param sql:
        :param environment:
        :return:
        """
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("this is OK!")
        except Exception as e:
            self.conn.rollback()
            print("Failed", e)
        self.cur.close()

eq = ExecuteSql()

if __name__ == '__main__':

    sql = "select sum(la.apply_no) apply_num,la.gather_type, la.alloc_date " \
          "from dm.dm_customer_learning_apply_info la " \
          "where la.alloc_date = '2020-03-06' " \
          "group by la.gather_type, la.alloc_date " \
          "order by la.gather_type"

    result = eq.query(sql)
    print(result)
    # x = []
    # y = []
    # for i in range(len(result)):
    #     if flowType == result[i]['gather_type']:
    #         flowNum = result[i]['apply_num']
    # print(x,y)



