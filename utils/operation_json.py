#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 15:28
# @Author  : LOUIE

import json
from config.read_config import rc
import os
from common.config_log import log

class OperationJson:

    def __init__(self, file="mainlink.json"):
        self.JSON_PATH = os.path.join(rc.PROJECT_PATH, "config", "json", file)

    def write_to_res_json(self, globals_var):

        with open(self.JSON_PATH, "w+", encoding="utf-8") as f:
            data = json.dumps(globals_var, indent=1, ensure_ascii=False)
            f.write(data)

    def get_from_json(self, key):

        with open(self.JSON_PATH, "r+", encoding="utf-8") as f:
            data = json.load(f)
        if key in data.keys():
            return data.get(key)
        else:
            log.error("key值不存在，请检查key: %s" %key)


if __name__ == '__main__':
    v = OperationJson().get_from_json("classTypeName")
    print(v)