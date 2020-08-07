# -*- coding:utf-8 -*-
#@Time : 2020/8/3 11:23
#@Author: Fold
#@File : test.py
import datetime
import time
import unittest

from pip._vendor.progress.counter import Counter
from six import assertCountEqual

from common.common_tools import cotool
from common.http_requests import httprequest
from utils.ExecuteSql import eq
from utils.get_api_data import get_data
from utils.login import login


class Test(unittest.TestCase):

    def setUp(self):
        login.login('m15656900011', '123456')
        self._data = get_data.get_yunyi_data('trafficTypeDataView.yaml')


    def test_traffic_type_data_view(self):
        login.login('m15656900011', '123456')
        self._data = get_data.get_yunyi_data('trafficTypeDataView.yaml')
        data = self._data.get('traffic_typ_dataview')
        url, method, header, params, sql, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        result = eq.query(sql)
        for i in range(len(result)):
            check['rows'][i]['flowNum'] = result[i]['apply_num']
        cotool.assert_list(res, check, 'rows')


    def test_traffic_trend_date_view(self):
        '''
        售前分公司维度
        :return:
        '''
        login.login('m15656900011', '123456')
        self._data = get_data.get_yunyi_data('trafficTypeDataView.yaml')
        data = self._data.get('traffic_trend_dataview')
        url, method, header, params, sql, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        result = eq.query(sql)
        check['data'][6 ]['day'] = result[0]['alloc_date']
        for i in range(len(result)):
            check['data'][6-i]['num'] = result[i]['apply_num']
        for j in range(6):
            check['data'][5-j]['day'] = check['data'][6-j]['day'] + datetime.timedelta(seconds = -1)
        for x in range(7):
            check['data'][x]['day'] = check['data'][x]['day'].strftime('%Y-%m-%d')
        cotool.assert_list(res, check, 'data')

    def test_traffic_trend_group_date_view(self):
        '''
        每日流量申请机构分组统计
        :return:
        '''
        login.login('m15656900011', '123456')
        self._data = get_data.get_yunyi_data('trafficTypeDataView.yaml')
        data = self._data.get('traffic_trend_group_dataview')
        url, method, header, params, sql, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        result = eq.query(sql)
        check['orgList'] = result
        cotool.assert_list(res, check, 'orgList')


if __name__ == '__main__':
    unittest.main()
    # Test().test_traffic_type_data_view()