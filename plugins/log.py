#!/usr/bin/python3
# -*- coding: utf-8

import time

class Log:
    '''
    DeBug日志 替代print
    '''
    # INFO 级别日志
    def info(info):
        print("INFO:",info)
    # 时间戳
    def time():
        print("TIME:",time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())
        ))

log = Log()