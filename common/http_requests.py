#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:37
# @Author  : LOUIE

from common.config_log import log
import requests
import json


class HttpRequest():

    def __init__(self):
        self.session = requests.session()

    def send_request(self, url, method, headers=None, data=None, cookies=None, **kwargs):
        """
        发起 http 请求：
        首先判断 method 请求方法，如果是 post 方法， 依据头部中的 content-type 字段判断传参方式

        eg: request = HttpRequests()
            response = request(method, url, data)
            or
            response = request.send_request(method, url, data)
            print(response.text)

        :param url: 完整请求地址
        :param method: 请求方法，默认post请求
        :param headers: 请求头部信息
        :param data: 请求正文
        :param cookies: cookies信息，非必传
        :return:
        """

        method = method.upper()
        log.info("请求地址: %s" % url)
        log.info("请求方法: [- %s -]" % method)
        log.info("请求头部: %s" % headers)
        if cookies:
            log.info("Set Cookies: %s" % cookies)
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                data = eval(data)
        log.info("请求正文: %s" % data)
        if method == "POST":
            # 依据头部被信息中的 content-type 判断传参方式
            if headers["content-type"] == "application/x-www-form-urlencoded":
                response = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
            elif headers["content-type"] == "application/json":
                response = requests.post(url=url, json=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
            else:
                response = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
        elif method == "GET":
            response = requests.get(url=url, params=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
        else:
            print("Method 值错误，请检查!!!")
        try:
            if response.status_code == 200:
                log.info("响应消息: %s" % response.json())
                return response.json()
        except json.decoder.JSONDecodeError:
            return response
        except Exception as e:
            log.error("Error: %s" % e)
        return response


    def __call__(self, url, method, headers=None, data=None, **kwargs):
        """
        示例，可以直接通过类对象实例直接调用此方法
        request = HttpRequests()
        response = request(method, url, data)
        """
        return self.send_request(url, method, headers, data, **kwargs)


    def close_session(self):
        '''
        关闭session请求方法
        :return:
        '''
        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass


httprequest = HttpRequest()


if __name__ == '__main__':
    from urllib3 import encode_multipart_formdata
    file = open('D:\Windows 10 Documents\Desktop\www.xlsx', mode='rb')
    payload = {
        "type": '1',
        "file": file.read()
    }
    encode_data = encode_multipart_formdata(payload)
    print(encode_data)
    header = {
        'content-type': encode_data[1],
        'token': '0x77f8760712ef2ec293142ad92eae79',
        'terminaltype': '4'
    }
    # print(payload)
    method = 'POST'
    url = 'https://galaxy-api-fat.shiguangkey.com/api/galaxy/grgz/cost/countDay/importing'
    # res = httprequest(url, method, header, payload)
    res = requests.post(url=url, headers=header, data=encode_data[0])
    print(res.json())
