#!/usr/env/bin/ python3
# -*- coding: utf-8 -*-

from aip import AipOcr
"安装：pip install baidu-aip"
""" 你的 APPID AK SK """
APP_ID = '14809450'
API_KEY = 'Qk3iML26p5l6e2amVGt5MUp8'
SECRET_KEY = 'eRnidVH4PQCys0WgP3hM9pdtDZ2lghz1'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 测试文件也可以写路径
image = get_file_content(r'E:\\CheckCode.jpg')

#  调用通用文字识别, 图片参数为本地图片
result = client.basicGeneral(image)

# 定义参数变量
options = {
    # 定义图像方向
        'detect_direction' : 'true',
    # 识别语言类型，默认为'CHN_ENG'中英文混合
        'language_type' : 'CHN_ENG',
}
# 调用通用文字识别接口
results = client.basicGeneral(image,options)
print(results)

# 遍历取出图片解析的内容
# for word in result['words_result']:
#     print(word['words'])
try:
    code = results['words_result'][0]['words']
except:
    code = '验证码匹配失败'

print(code)
