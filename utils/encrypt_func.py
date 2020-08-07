#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:59
# @Author  : LOUIE


import hashlib
import base64


def md5_digest(string):

    md5 = hashlib.md5()
    if not isinstance(string, bytes):
        string = str(string).encode('utf-8')
    md5.update(string)
    return md5.digest()

def encrypt_passwd(passwd):
    passwd = str(passwd)
    md5 = md5_digest(string=passwd)
    passwd64 = base64.b64encode(md5)
    passwd64= str(passwd64.decode()).replace('=', '')
    print(passwd64)
    return passwd64

if __name__ == '__main__':
    string = "123456"
    encrypt_passwd(string)

