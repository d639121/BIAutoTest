#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 10:43
# @Author  : LOUIE

import yaml
import os
from config.read_config import rc


class GetApiData():

    def __init__(self):
        pass

    def get_yaml(self, yaml_path):

        if not yaml_path.endswith(".yaml"):
            yaml_path = str(yaml_path) + ".yaml"
        api_yaml_path = os.path.join(rc.PROJECT_PATH, "data\\api", yaml_path)
        with open(api_yaml_path, mode="r", encoding="utf-8") as file:
            data = yaml.full_load(file)
        return data

    def _get_yaml_path(self, module, yaml_path):

        api_yaml_path = os.path.join(rc.PROJECT_PATH, 'data\\api', module, yaml_path)
        with open(api_yaml_path, mode="r", encoding="utf-8") as file:
            data = yaml.full_load(file)
        return data

    def get_api_data(self, params):
        desc = []
        url = []
        parameterize = []
        method = []
        header = []
        param = []
        check = []
        sql = []
        desc.append(params.get("desc", None))
        url.append(rc.set_environment(params["url"]))
        parameterize.append(params.get("parameterize", None))
        method.append(params.get('method'))
        header.append(params.get("header", None))
        param.append(params.get("data", None))
        sql.append(params.get("sql", None))
        check.append(params.get("check", None))
        listdata = list(zip(desc, parameterize, url, method, header, param, sql, check))[0]
        return listdata

    def get_haichuan_data(self, yaml_path):
        data = self._get_yaml_path('haichuan', yaml_path)
        return data

    def get_yinhe_data(self, yaml_path):
        data = self._get_yaml_path('yinhe', yaml_path)
        return data

    def get_base_data(self, yaml_path):
        data = self._get_yaml_path('base', yaml_path)
        return data

    def get_yunyi_data(self, yaml_path):
        data = self._get_yaml_path('yunyi', yaml_path)
        return data

get_data = GetApiData()


if __name__ == '__main__':
    data = get_data.get_base_data('login_account.yaml')
    print(data)
    import re
    compile = re.compile(r'\$<(\w+?)>')
    res = compile.findall(str(data))
    from config.constant import GLOBAL_VAR
    from utils.get_value import gv
    glob = {}
    for i in res:
        glob[i] = GLOBAL_VAR[i]
    data = gv.resolve_global_var(data, glob)
    print(data)
