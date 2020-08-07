#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:47
# @Author  : LOUIE

from common.common_tools import cotool
from utils.get_api_data import get_data
from config.constant import GLOBAL_VAR
from common.http_requests import httprequest
from utils.encrypt_func import encrypt_passwd


class Login():

    def __init__(self):
        self._data = get_data.get_base_data('login_account.yaml')

    def login(self, account=None, password=None, type='pt'):
        '''
        潭州平台登录
        :param kwargs:
        :return:
        '''
        if type == 'pt' or type == 'platform':
            data = self._data['tz_platform_account']
        elif type == 'phone':
            data = self._data['tz_platform_account']
        else:
            data = self._data['tz_classroom_account']
        url, method, header, params, shared, check = cotool.deal_data(data)
        if account is not None:
            params['account'] = account
        if password is not None:
            params['password'] = encrypt_passwd(password)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        token = res['data']['token']
        GLOBAL_VAR['token'] = token
        return token


login = Login()


if __name__ == '__main__':
    login.login()
    print(GLOBAL_VAR['token'])
