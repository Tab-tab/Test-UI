import time
import os
from selenium import webdriver
from utils.config import DriverPath, ReportPath
from HTMLReport import addImage

# 根据传入的参数选择浏览器的driver去打开对应的浏览器

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DriverPath + '\chromedriver.exe'
IEDRIVER_PATH = DriverPath + '\IEDriverServer.exe'  # 不存在
PHANTOMJSDRIVER_PATH = DriverPath + '\phantomjs.exe'  # 不存在

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    # 截图
    def screen_shot(self):
        time.sleep(1)
        addImage(self.driver.get_screenshot_as_base64())
        time.sleep(1)

    def close(self):

        self.driver.close()

    def quit(self):

        self.driver.quit()


# 这里试验了一下保存截图的方法，保存png截图到report目录下。
if __name__ == '__main__':
    b = Browser('chrome').get('http://www.baidu.com')
    b.screen_shot('test_baidu')
    time.sleep(3)
    b.quit()
