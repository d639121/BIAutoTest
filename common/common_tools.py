#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 10:12
# @Author  : LOUIE
import jsonpath

from common.config_log import log
from config.constant import const,GLOBAL_VAR
from utils.get_api_data import get_data
from utils.get_value import gv
from config.read_config import rc
from common.http_requests import httprequest


class CommonTools:

    def assert_res(self, res, check):
        '''
        断言方法
        当 check 为 no_check、no和 None 时跳过断言
        当 check 为 dict 类型时, 判断字段是否存在于 code 和 entity 字典中,进行断言
        :param res: 响应内容 response
        :param check: YAML文件中的 check 节点数据
        :return: None
        '''
        code = ['code', 'status', 'res', 'msg']
        entity = ['data', 'result']
        if check == "no_check" or "no" in check or check is None:
            log.info("This Api Has No Check!")
        elif isinstance(check, dict):
            for k,j in check.items():
                if k in code:
                    acode = res[k]
                    ecode = check[k]
                    assert str(acode) == str(ecode)
                    log.info('校验类型: [-{}], 结果: [Passed], 预期: [{}]'.format(k, str(ecode)) )
                if k in entity:
                    data = res[k]
                    for check_param in check["data"]:
                        if isinstance(check_param, dict):
                            for k, v in check_param.items():
                                if k == 'in':
                                    if len(v) >= 1:
                                        for i in v:
                                            assert i in str(data)
                                if k == 'eq':
                                    for j, h in v.items():
                                        assert h == gv.get_jsonpath_value(data, j)
                                        log.info('校验类型: [-{}], 结果: [Passed], 预期: {}'.format(k, v))
                                if k == 'tag':
                                    assert GLOBAL_VAR[v] in str(data)
                                    log.info('校验类型: [-{}], 结果: [Passed], 预期: {}'.format(k, GLOBAL_VAR[v]))
                        elif isinstance(check_param, str):
                            assert check_param in str(data)
                            log.info('校验类型: [-in], 结果: [Passed], 预期: [{}]'.format(check_param))
                        else:
                            print('请输入正确校验数据格式！！')
        else:
            print("YAML文件中 check 非字典类型，类型错误！")
        log.info('    ' * 5 + ' = = = ' * 8 + '分割线' + ' = = =' * 8)

    def assert_list(self, res, check, key):
        '''
        校验列表数据方法
        :param res: response返回的json数据
        :param check: 预期结果
        :param key: 校验的字段，key
        :return:
        '''
        if res['status'] == '0':
            res1 = jsonpath.jsonpath(res, '$..%s' % key)
            act = res1[0]
            exp = check[key]
            if ((len(act) == len(exp)) and
                    (all(i in act for i in exp))):
                log.info('校验类型: [-in], 结果: [Passed], 预期: {}'.format(exp))
            else:
                log.info('校验类型: [-in], 结果: [Failed], 实际: {}'.format(act))
        else:
            log.info('校验类型: [-in], 结果: [Failed], 实际: {}'.format(res))


    def extract_variable(self, res, shared):
        '''
        提取变量方法 期望值
        :param res: 响应内容response
        :param shared: 提取response中的参数名
        :return:
        '''
        # 通过判断shared字段是否为空，得出是否需要取值，为空则跳过
        if shared is not None:
            # 如果不为空，则遍历shared字典，进行response取值
            for k, v in shared.items():
                if "-" not in v:
                    value = gv.get_jsonpath_value(res, v)
                else:
                    key, num = str(v).split("-")
                    value = gv.get_jsonpath_value(obj=res, key=key, num=int(num))
                setattr(const, k, value)
                GLOBAL_VAR[k] = value
                log.info("提取变量: [ {}: {} ]".format(k, value))

    def set_params(self, parameterize, params):
        '''
        参数化处理数据
        :param parameterize:
        :param params:
        :return:
        '''
        data = None
        if parameterize is not None:
            for k, v in parameterize.items():
                parameterize[k] = GLOBAL_VAR[v]
                data = gv.resolve_global_var(params, parameterize)
            return data
        else:
            return params

    def set_header(self, header):
        '''
        处理header中的token方法
        :param header: 原生header数据
        :return:
        '''
        if header is not None:
            if "token" in header.keys():
                users = ['partner', 'leader', 'students', 'student']
                token = str(header['token']).replace('$<', '').replace('>', '')
                print(token)
                header["token"] = GLOBAL_VAR.get(token, GLOBAL_VAR['leader'])
            elif "cookie" in header.keys():
                header["cookie"] = GLOBAL_VAR.get('cookie', rc.get_token("cookie"))
            # 解决多次调用查询时报的主机拒绝远程连接的错误
            # if "user-agent" not in header.keys():
            #     header["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
            # header["Connection"] = "close"
            # header["keep-alive"] = "False"
            return header
        else:
            return header


    def get_pre_data(self, file, name):
        pass

    def deal_data(self, data):
        '''
        封装整体方法
        :param data: 传入的数据
        :return: None
        '''
        data = get_data.get_api_data(data)
        desc, parameterize, url, method, header, param, sql, check = data
        log.info('描述信息: %s' % desc)
        header = self.set_header(header)
        params = self.set_params(parameterize, param)
        return url, method, header, params, sql, check

    def handle_param(self, data, **kwargs):
        '''
        封装整体方法
        :param data: 传入的数据
        :return: None
        '''
        data = get_data.get_api_data(data)
        desc, parameterize, url, method, header, param, shared, check = data
        log.info('描述信息: %s' % desc)
        header = self.set_header(header)
        params = self.set_params(parameterize, param)
        if kwargs:
            for k, v in kwargs.items():
                params[k] = v
        res = httprequest(url, method, header, params)
        self.extract_variable(res, shared)
        self.assert_res(res, check)
        return res


cotool = CommonTools()
