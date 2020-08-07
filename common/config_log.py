#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 16:01
# @Author  : LOUIE

import logging
from logging.handlers import TimedRotatingFileHandler
import threading
import time
import os
import functools
from config.read_config import rc


class ConfiLog:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 日志显示样式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")

        # 构建日志路径结构
        date = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        log_path = os.path.join(rc.PROJECT_PATH,  "report/log")
        if not os.path.exists(log_path):    # 如果路径不存在则创建
            os.mkdir(log_path)
        # 完整日志存放路径
        all_log_path = os.path.join(log_path, "all_log")
        all_log_name = all_log_path + "\\" + date + ".log"
        if not os.path.exists(all_log_path):    # 如果路径不存在则创建
            os.mkdir(all_log_path)
        # 错误日志存放路径
        error_log_path = os.path.join(log_path, "error_log")
        error_log_name = error_log_path + "\\" + date + ".log"
        if not os.path.exists(error_log_path):  # 如果路径不存在则创建
            os.mkdir(error_log_path)

        # # 日志写入Handler
        #         # fh = logging.FileHandler(all_log_name)
        #         # fh.setLevel(logging.INFO)
        #         # fh.setFormatter(formatter)
        #         # self.logger.addHandler(fh)

        # # 错误日志写入Handler
        # eh = logging.FileHandler(error_log_name)
        # eh.setLevel(logging.ERROR)
        # eh.setFormatter(formatter)
        # self.logger.addHandler(eh)

        # 控制台输出Handler
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        self.logger.addHandler(sh)

        # # 当日志需要循环写入时，可以使用TimedRotatingFileHandler， 设置when为“D”
        # fh = TimedRotatingFileHandler(filename=all_log_name, when="M", backupCount=2, interval=1, encoding="utf-8")
        # fh.setLevel(logging.DEBUG)
        # fh.setFormatter(formatter)
        # self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger


class MyLog:

    Log = None
    mutex = threading.Lock()

    @staticmethod
    def get_log():
        if MyLog.Log is None:
            MyLog.mutex.acquire()
            MyLog.Log = ConfiLog()
            MyLog.mutex.release()
        return MyLog.Log


mylog = MyLog.get_log()
# 实例化ConfigLog对象，方便调用
log = mylog.get_logger()


def logger(param=None):
    '''
    日志记录装饰器
    调用方法: @logger()
    :param param: 传入对应的参数可输出对应的信息。例如输入'Class', 会指定执行lif param == 'class':中的代码
    :return:
    '''
    if callable(param):
        def wrapper(*args, **kw):
            log.info('正在执行啊啊Function: {}'.format(func.__name__))
            param(*args, **kw)
        return wrapper

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):

            if param == 'case':
                log.info('当前运行Case: {}'.format(func.__name__))
            if param == 'block':
                log.info('正在执行Block: {}'.format(func.__name__))
            elif param == 'class':
                desc = str(func.__doc__).strip()
                log.info('当前所在Class: {} || 类描述信息: {}'.format(func.__name__, desc))
            else:
                log.info('正在执行Function: {}'.format(func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


if __name__ == '__main__':
    log.info('test message!')