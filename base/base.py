from selenium import webdriver
import os, time

# current_path当前地址
CurrentPath = os.path.abspath(os.path.dirname(__file__))

# project_path 项目根目录地址
ProjectPath = os.path.split(CurrentPath)[0]

# 工具地址
ToolsPath = ProjectPath.replace("\\", "/") + "/driver/chromedriver"

driver = webdriver.Chrome(ToolsPath)

driver.get("http://www.baidu.com")

time.sleep(3)
driver.close()
