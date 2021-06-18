from selenium.webdriver.common.action_chains import ActionChains
from driver.browser import Browser
from HTMLReport import logging, addImage
import time
from utils.config import Config

# 不能删除
from selenium.webdriver.common.by import By

import os
BasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


# 浏览器页面类，主要进行浏览器页面的控制，包括获取
class Page(Browser):
    def __init__(self, page=None, browser_type='chrome', pagefile=None):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)
        self.config_page = Config()

        pages_yml_file = self.config_page.get('pages_yml_file')
        elpage = Config(os.path.join(BasePath, 'pages', pages_yml_file + ".yml")).get(pagefile)
        self.el = Config(os.path.join(BasePath, 'pages', elpage + ".yml"))

    # 获取当前窗口句柄
    @property
    def current_window(self):
        return self.driver.current_window_handle

    # 获取标题
    @property
    def title(self):
        return self.driver.title

    # 获取当前网址
    @property
    def current_url(self):
        return self.driver.current_url

    # 获取浏览器驱动
    def get_driver(self):
        return self.driver

    # 睡眠一段时间
    def wait(self, seconds=3):
        time.sleep(seconds)

    # 执行js脚本
    def execute(self, js, *args):
        self.driver.execute_script(js, *args)

    # 移动到指定元素
    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # 寻找指定元素
    def find_element(self, *args):
        return self.driver.find_element(*args)

    # 寻找指定的一批元素
    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    # 切换窗口
    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logging.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logging.debug(self.driver.current_url, self.driver.title)

    # 切换frame页面
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    # 切换alter
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    # 打开浏览器输入网址
    def setUrl(self, url):
        url = self.config_page.get(url)
        self.driver.get(url)

    # 获取元素跟据不同的类型查找方式查找，需要后期增加
    def page_el(self, str_el):
        logging.info("元素名称" + str_el)
        eltype = str_el.split('_')[2]
        if eltype == 'xpath':
            str_el = "(By.XPATH,'" + self.el.get("pages")[str_el] + "')"
            logging.info("查找元素" + str_el)
            el = self.find_element(*eval(str_el))
        if eltype == 'id':
            str_el = "(By.ID,'" + self.el.get("pages")[str_el] + "')"
            logging.info("查找元素" + str_el)
            el = self.find_element(*eval(str_el))
        return el
