#! /usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os

# 获取当前系统时间的字符串
local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 获取当前时间年份
year = time.strftime('%Y', time.localtime(time.time()))
# 获取当前时间月份
month = time.strftime('%m', time.localtime(time.time()))
# 获取当前时间天份
day = time.strftime('%d', time.localtime(time.time()))

# 获取当前时间-小时
hour = time.strftime('%H', time.localtime(time.time()))
# 获取当前时间-分钟
minute = time.strftime('%M', time.localtime(time.time()))
# 获取当前时间-秒
second = time.strftime('%S', time.localtime(time.time()))

# 年、月、日 路径
FileYear = '../report/' + '/' + year
FileMonth = FileYear + '/' + month
FileDay = FileMonth + '/' + day


def file_name():
    if not os.path.exists(FileYear):
        os.mkdir(FileYear)
        os.mkdir(FileMonth)
        os.mkdir(FileDay)
    else:
        if not os.path.exists(FileMonth):
            os.mkdir(FileMonth)
            os.mkdir(FileDay)
        else:
            if not os.path.exists(FileDay):
                os.mkdir(FileDay)
    return FileDay


def report_name():
    return year + month + day + hour + minute + second
