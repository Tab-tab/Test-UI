import unittest, os, time
from driver.page import Page
from selenium import webdriver
from utils.config import Config

# 基础路径
BasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# 配置路径
ConfigFile = os.path.join(BasePath, 'config', 'config.yml')

DataPath = os.path.join(BasePath, 'data')

DriverPath = os.path.join(BasePath, 'driver/chromedriver')

ReportPath = os.path.join(BasePath, 'report')

PagesPath = os.path.join(BasePath, 'pages')

LogPath = os.path.join(BasePath, 'log')

# data yml
homepage_data_path = os.path.join(PagesPath, 'homepage.yml')
journalism_data_path = os.path.join(PagesPath, 'journalismpage.yml')


class TestLogin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    # @classmethod
    # def setUpClass(cls):
    #     cls.home_page = Page(pagefile="homepage", browser_type='chrome').get("https://www.baidu.com")
    #     cls.journalism_page = Page(page=cls.home_page, pagefile="journalismpage")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.home_page.close()
    #
    # def tearDown(self):
    #     self.home_page.screen_shot()

    def setUp(self):

        home_url = Config(homepage_data_path).get("url")

        self.driver = webdriver.Chrome(executable_path=DriverPath)
        self.driver.get(home_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def tearDown(self):
        self.driver.quit()

    def test01(self):
        home_pages_dict = Config(homepage_data_path).get("pages")
        self.driver.find_element_by_xpath(home_pages_dict["journalism_by_xpath"]).click()
        driver_handle = self.driver.window_handles
        self.driver.switch_to.window(driver_handle[-1])

        jour_pages_dict = Config(journalism_data_path).get("pages")
        self.driver.find_element_by_xpath(jour_pages_dict["girl_by_xpath"]).click()
        self.driver.find_element_by_xpath(jour_pages_dict["baiduinput_by_xpath"]).send_keys("蔡依林")
        self.driver.find_element_by_xpath(jour_pages_dict["baidubotton_by_xpath"]).click()
        time.sleep(3)

    def test02(self):
        home_pages_dict = Config(homepage_data_path).get("pages")
        self.driver.find_element_by_xpath(home_pages_dict["journalism_by_xpath"]).click()
        driver_handle = self.driver.window_handles
        self.driver.switch_to.window(driver_handle[-1])

        jour_pages_dict = Config(journalism_data_path).get("pages")
        self.driver.find_element_by_xpath(jour_pages_dict["girl_by_xpath"]).click()
        self.driver.find_element_by_xpath(jour_pages_dict["baiduinput_by_xpath"]).send_keys("黄连")
        self.driver.find_element_by_xpath(jour_pages_dict["baidubotton_by_xpath"]).click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
