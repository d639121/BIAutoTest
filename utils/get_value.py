#! /usr/bin/python
# coding:utf-8

import jsonpath
import json
import re


class GetValues(object):

    def __init__(self):
        pass

    def get_jsonpath_value(self, obj, key, num=0):

        if "$" not in key:
            expr = "$..{}".format(str(key))
            if '-' in key:
                key, num = str(key).split('-')
            value = jsonpath.jsonpath(obj=obj, expr=expr)[num]
            return str(value)
        else:
            print("已有匹配符， 请勿输入")


    def dict_get(self, dic, locators, default=None):

        if not isinstance(dic, dict) or not isinstance(locators, list):
            return default

        value = None

        for locator in locators:
            if not type(value) in [dict, list] and isinstance(locator, str) and not self.can_convert_to_int(locator):
                try:
                    value = dic[locator]
                except KeyError:
                    return default
                continue
            if isinstance(value, dict):
                try:
                    value = self.dict_get(value, [locator])
                except KeyError:
                    return default
                continue
            if isinstance(value, list) and self.can_convert_to_int(locator):
                try:
                    value = value[int(locator)]
                except IndexError:
                    return default
                continue

        return value

    def can_convert_to_int(self, input):
        try:
            int(input)
            return True
        except BaseException:
            return False


    def replace_target_Value(self, key, dic, changeData):

        if isinstance(dic, str):
            try:
                dic = json.loads(dic)
            except Exception:
                dic = eval(dic)
        if not isinstance(dic, dict):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '
        if key in dic.keys():
            dic[key]=changeData # 修改字典
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    self.replace_target_Value(key, value, changeData)  # 传入数据的value值是字典，则直接调用自身，将value作为字典传进来
                    # value[key]=changeData   #替换key的value
                elif isinstance(value, (list, tuple)):
                    self.replace_target(key, value, changeData)  # 传入数据的value值是列表或者元组，则调用replace_target
        return dic


    def replace_target(self,key, val, changeData):

        for val_ in val:
            if isinstance(val_, dict):
                self.replace_target_Value(key, val_, changeData)  # 传入数据的value值是字典，则调用replace_target_Value
            elif isinstance(val_, (list, tuple)):
                self.replace_target(key, val_, changeData)   # 传入数据的value值是列表或者元组，则调用自身


    # 解析字符串中全局变量并进行替换
    def resolve_global_var(self, raw_var, global_var, regex='\$<.*?>', sub_start_index=2, sub_end_index=-1):

        raw_var = json.dumps(raw_var)
        if not isinstance(raw_var, str):
            raise TypeError('raw_var must be str！')

        if not isinstance(global_var, dict):
            raise TypeError('global_var must be dict！')

        if not isinstance(regex, str):
            raise TypeError('regex must be str！')

        if not isinstance(sub_start_index, int):
            raise TypeError('sub_start_index must be int！')

        if not isinstance(sub_end_index, int):
            raise TypeError('sub_end_index must be int！')

        re_global_var = re.compile(regex)

        def global_var_repl(match_obj):
            start_index = sub_start_index
            end_index = sub_end_index
            match_value = global_var.get(match_obj.group()[start_index:end_index])
            return match_value if match_value else match_obj.group()

        resolved_var = re.sub(pattern=re_global_var, string=raw_var, repl=global_var_repl)
        try:
            data = json.loads(resolved_var)
        except Exception:
            data = eval(resolved_var)
        return data


gv = GetValues()


if __name__ == '__main__':
    tmp_dic={
                'respCode': '0000',
                'message': 'success',
                'data': {
                    'totalCount': 9527,
                    'totalPage': 1,
                    'items': [{
                        'publishTime': 12345678910,
                        'totalAmount': 0,
                        'projectId': '789'
                    },
                        {
                        'publishTime': 12345,
                        'totalAmount': 1,
                        'projectId': '20'
                        }
                    ]
                }
            }
    value = {"9527": "123456"}
    resolve_data = gv.replace_target_Value('message', tmp_dic, '57185181850095616')

    print(resolve_data)
