from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HTMLTestRunner import HTMLTestRunner

# 定义了By方式，显示等待，期待状况另命名EC
import os, time
import unittest

# 公共路径部分
# 当前路径
CurrentPath = os.path.abspath(os.path.dirname(__file__))

# 根目录
ProjectPath = os.path.split(CurrentPath)[0]

# 驱动路径
ToolPath = ProjectPath.replace("\\", "/") + "/driver/chromedriver"


# 登陆模块
class Login(unittest.TestCase):

    # 准备工作

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ToolPath)
        # self.driver.maximize_window()
        # Url地址 http://172.8.10.129/
        login_url = "http://172.8.10.129"
        # 隐式等待，超时报错
        self.driver.implicitly_wait(35)
        try:
            self.driver.get(login_url)
            # time.sleep(5)
            checking_msg = self.driver.find_element_by_class_name('login_btn').text
            print('=========={}=========='.format(checking_msg))
            self.assertEqual(checking_msg, "登录", msg="验证打开页面False")

        except Exception:
            print("-----------{}--------------".format("打开页面失败"))
        else:
            print("-------{}-------".format("打开页面成功"))

    def TestLogin(self):
        user_name = 'Demo01'
        user_password = '123456'
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div[1]/input'
            ).send_keys(user_name)

            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[1]/input'
            ).send_keys(user_password)
            self.driver.find_element_by_class_name("login_btn").click()

            # 消息中心Xpath
            # meg_xpath = '//*[@id="app"]/div/div/div[2]/div[1]/div/div/span[2]'
            # text_to_be_present_in_element：等待含有指定字符串的元素
            # WebDriverWait(self.driver, timeout=10).until(EC.text_to_be_present_in_element((By.XPATH, meg_xpath)))

            # current_url = self.driver.current_url
            # home_url = "http://172.8.10.129/#/home"
            # self.assertEqual(current_url, home_url, msg="验证主页失败")
            # time.sleep(5)

        except:
            print("---------{}---------".format('登陆进入主页失败'))
        else:
            print("---------{}---------".format('登陆进入主页成功'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login("TestLogin"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()


