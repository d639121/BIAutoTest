# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

关于Excel表的操作
'''
import os

import xlrd
from config.read_config import rc


class ExcelHandler(object):


    def get_excel_data(self, xls_name, sheet_name):
        xls_data = []
        # 构建xls_path路径
        xls_path = os.path.join(rc.PROJECT_PATH, 'testdata', xls_name)
        book = xlrd.open_workbook(xls_path)
        # 获取到book对象
        # book = xlrd.open_workbook(conf.TEST_CASE_PATH)
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        sheet = book.sheet_by_name(sheet_name)
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols

        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            xls_data.append(dict(zip(title, sheet.row_values(i))))
        return xls_data
