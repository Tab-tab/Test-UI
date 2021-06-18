#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from utils.reader_file import YamlReader

# 基础路径
BasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# 配置路径
ConfigFile = os.path.join(BasePath, 'config', 'config.yml')

DataPath = os.path.join(BasePath, 'data')

DriverPath = os.path.join(BasePath, 'driver')

ReportPath = os.path.join(BasePath, 'report')

PagesPath = os.path.join(BasePath, 'pages')

LogPath = os.path.join(BasePath, 'log')


class Config:
    def __init__(self, config=ConfigFile):
        print('配置文件地址', config)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
            yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
            这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)


if __name__ == '__main__':
    url = Config(PagesPath).get("homepage")
    print(url)
