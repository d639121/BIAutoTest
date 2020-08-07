#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 16:00
# @Author  : LOUIE

from configparser import ConfigParser
import os
import re


class ReadConifg:

    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(PROJECT_PATH, "config", "config.ini")
    REPORT_PATH = os.path.join(PROJECT_PATH, "report")
    # 导入/上传excel文件路径
    EXCEL_PATH = os.path.join(PROJECT_PATH, "config\\excel" )

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(self.CONFIG_PATH, encoding="utf-8")

    def get_email(self, option):

        value = self.cf.get("EMAIL", option)
        return value

    def get_db(self, option):

        value = self.cf.get("DB", option)
        return value

    def get_env(self):

        value = self.cf.get("ENV", "environment")
        return str(value).lower()

    def get_report(self, option):

        value = self.cf.get("REPORT", option)
        return value

    def get_token(self, option):

        value = self.cf.get("TOKEN", option)
        return value

    def set_section(self, section):

        self.cf.add_section(section)

    def set_value(self, section, option, value):

        section = self.set_section(section)
        self.cf.set(section, option, value)

    def set_token(self, option, value):

        self.cf.set(section='TOKEN', option=option, value=value)
        with open(self.CONFIG_PATH, 'w+', encoding='utf-8') as f:
            self.cf.write(f)

    def get_account_info(self, env):

        partner = self.cf.get('ACCOUNT', "{}_partner".format(env))
        leader = self.cf.get('ACCOUNT', "{}_leader".format(env))
        students = self.cf.get('ACCOUNT', "{}_student".format(env))
        cookie = self.cf.get('ACCOUNT', "{}_cookie".format(env))
        return partner,leader,students,cookie

    def set_environment(self, url):

        env = self.get_env()
        compile = re.compile(r'(test)|(fat)|(pre)')
        pattern = compile.search(url)
        if pattern is not None:
            pattern = pattern.group()
            new_url = url.replace(pattern, env)
        else:
            new_url = url
        return new_url


rc = ReadConifg()


