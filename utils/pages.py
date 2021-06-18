#! /usr/bin/env python
# -*- coding: utf-8 -*-

from utils.config import Config
import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


class PageEl:

    def __init__(self, page):
        pages_ymlfile = Config().get('pages_ymlfile')
        el_page = Config(os.path.join(BASE_PATH, 'pages', pages_ymlfile+".yml")).get(page)
        self.el = Config(os.path.join(BASE_PATH, 'pages', el_page+".yml"))

    def get(self, el):
        el_type = el.split('_')[2]
        if el_type == 'xpath':
            el = "(By.XPATH,'" + self.el.get("pages")[el] + "')"
        if el_type == 'ID':
            el = "(By.ID,'" + self.el.get("pages")[el] + "')"
        return el


if __name__ == "__main__":
    s = PageEl('login_page').get('username_by_xpath')
    print(s)
