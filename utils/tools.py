#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:27
# @Author  : LOUIE

from config.constant import GLOBAL_VAR
import qrcode
from config.read_config import rc
import easygui


def create_qr_code(creativityCode):

    link = "https://mz-test.tanzhouedu.com/?s={}".format(creativityCode)
    print(link)
    img_name = rc.PROJECT_PATH + "/config/img/meizi.png"
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(img_name)
    easygui.msgbox(msg='请扫码，完成付款后再点按钮', title='媒资落地页二维码', ok_button='已完成付款', image=img_name)

def create_code():

    creativityCode = GLOBAL_VAR['creativityCode']
    link = "https://mz-fat.tanzhouedu.com/?s={}".format(creativityCode)
    img_name = rc.PROJECT_PATH + "/config/img/meizi.png"
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(img_name)
    easygui.msgbox(msg='请扫码，完成付款后再点按钮', title='媒资落地页二维码', ok_button='已完成付款', image=img_name)


if __name__ == '__main__':
    create_code()
