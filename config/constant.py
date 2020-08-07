#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 10:16
# @Author  : LOUIE

from utils import generator
from config.read_config import rc
from datetime import date, timedelta
import time


class Const:

    referPrice="1000"
    floorPrice="800"
    discountsPrice= "888"
    userName='LOUIE'
    project = str("自动化计划{}".format(generator.random_ean8()))

    def __init__(self):
        account = 't0331433110'

    @property
    def timestamp(self):
        '''
        当前时间戳
        :return: 1595230844000
        '''
        return str(generator.timestamp())

    @property
    def title(self):
        '''
        标题
        :return: 自动化测试95277114
        '''
        return str("自动化测试{}".format(generator.random_ean8()))

    @property
    def transNo(self):
        '''
        交易单号
        :return: 1595230844000
        '''
        return self.timestamp

    @property
    def project_Name(self):
        '''
        计划名称
        :return: 自动化计划95277114
        '''
        return str("自动化计划{}".format(generator.random_ean8()))

    @property
    def phoneNumber(self):
        '''
        手机号
        :return: 13347335633
        '''
        return str(generator.random_phone_number())

    @property
    def qq(self):
        '''
        qq号
        :return: 95277114
        '''
        return str(generator.random_ean8())

    @property
    def tomorrow(self):
        '''
        当前日期 + 1，明天
        :return:
        '''
        return str((date.today() + timedelta(days=+1)).strftime("%Y-%m-%d"))

    @property
    def yesterday(self):
        '''
        当前日期 - 1， 昨天
        :return:
        '''
        return str((date.today() + timedelta(days=-1)).strftime("%Y-%m-%d"))

    @property
    def courseName(self):
        '''
        课程名称
        :return: 自动化课程95277114
        '''
        return str("自动化课程{}".format(generator.random_ean8()))

    @property
    def classTypeName(self):
        '''
        小咖班型名称
        :return: 自动化班型95277114
        '''
        return str("自动化班型{}".format(generator.random_ean8()))

    @property
    def ideaName(self):
        '''
        银河创意名称
        :return: 自动化创意95277114
        '''
        return str("自动化创意{}".format(generator.random_ean8()))

    @property
    def goodsName(self):
        '''
        小咖商品名称
        :return: 自动化商品95277114
        '''
        return str("自动化商品{}".format(generator.random_ean8()))

    @property
    def channelName(self):
        '''
        银河渠道名称
        :return: 自动化渠道95277114
        '''
        return str("自动化渠道{}".format(generator.random_ean8()))

    @property
    def websiteName(self):
        '''
        银河落地页名称
        :return: 自动化落地页95277114
        '''
        return str("自动化落地页{}".format(generator.random_ean8()))

    @property
    def setTime(self):
        '''
        特殊时间格式
        :return: 2020-07-20T15:38:07Z
        '''
        return str(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(time.time())))

    @property
    def todayStartTime(self):
        '''
        当前日期起始点（格式化）
        :return: 2020-07-20 00:00:00
        '''
        return str(time.strftime("%Y-%m-%d 00:00:00", time.localtime()))

    @property
    def todayEndTime(self):
        '''
        当前日期截止点（格式化）
        :return: 2020-07-20 23:59:59
        '''
        return str(time.strftime("%Y-%m-%d 23:59:59", time.localtime()))


    @property
    def gatherTimeStart(self):
        '''
        当前日期起始点（时间戳）
        :return: 1595174400000
        '''
        return str(int(time.mktime(time.strptime(self.todayStartTime, "%Y-%m-%d %H:%M:%S"))) * 1000)

    @property
    def gatherTimeEnd(self):
        '''
        当前日期截止点（时间戳）
        :return: 1595260799000
        '''
        return str(int(time.mktime(time.strptime(self.todayEndTime, "%Y-%m-%d %H:%M:%S"))) * 1000)

    @property
    def todyTime(self):

        return str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))

    @property
    def partner(self):
        '''
        小伙伴 token
        :return:
        '''
        return rc.get_token("partner")

    @property
    def leader(self):
        '''
        负责人 token
        :return:
        '''
        return rc.get_token("leader")


const = Const()


GLOBAL_VAR = {

    "referPrice": "1000",
    "floorPrice": "800",
    "discountsPrice": "888",
    "userName": 'LOUIE',
    "qq": const.qq,
    "title": const.title,
    "transNo": const.transNo,
    "setTime": const.setTime,
    "leader": const.leader,
    "partner": const.partner,
    "phoneNumber": const.phoneNumber,
    "ideaName": const.ideaName,
    "goodsName": const.goodsName,
    "courseName": const.courseName,
    "projectName": const.project_Name,
    "websiteName": const.websiteName,
    "channelName": const.channelName,
    "classTypeName": const.classTypeName,
    "timestamp": const.timestamp,
    "yesterday": const.yesterday,
    "tomorrow": const.tomorrow,
    "payTimeStart": const.yesterday,
    "todayStartTime": const.todayStartTime,      # 2020-06-10 00:00:00
    "todayEndTime": const.todayEndTime,          # 2020-06-10 23:59:59
    "todayTime": const.todyTime,                 # 2020/06/10 16:25:36
    "gatherTimeStart": const.gatherTimeStart,    # 1591113600000
    "gatherTimeEnd": const.gatherTimeEnd,        # 1591718399999
    # ****** 教务课程初始化参数 *******
    "teachingGoodsid": "408",
    "teachingGoodsName": "哈哈哈",
    "teachingGoodsdesc": "11113313",
    "teachingGoodscover": "https://test-huawei-media.shiguangkey.com/kbhmgzuigtthvde",
    "teachingPriceOrigin": "0.01",
    "teachingPriceText": "0.01",
    "teachingCourseId": "19347",
    # ****** 小咖课程初始化参数 *******
    "xiaokaGoodsid": "418",
    "xiaokaGoodsName": "小咖批量入库测试01",
    "xiaokaGoodsdesc": "魔动闪吧",
    "xiaokaGoodscover": "https://xk-hd2.tanzhou.cn/file/edu/courseType/20200618/09/20200618093601396893822.jpg",
    "xiaokaPriceOrigin": "50",
    "xiaokaPriceText": "45",
    "xiaokaCourseId": "495",
    'login': '123124'
}


if __name__ == '__main__':
    print(GLOBAL_VAR)
    print(GLOBAL_VAR.copy())

