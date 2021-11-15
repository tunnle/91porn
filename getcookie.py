from selenium import webdriver
import time
import requests
import json
import os


def savecookies(cookies):
    with open(os.getcwd() + '\cookies.txt', 'w') as f:
        cookie = json.dumps(cookies)
        f.write(cookie)

url='http://807.workgreat17.live'

options = webdriver.ChromeOptions()
# 打开chrome浏览器
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
options.add_argument('--headless') # 无头模式
options.add_argument('--disable-gpu')
options.add_argument('--start-maximized')#最大化
options.add_argument('--incognito')#无痕隐身模式
options.add_argument("disable-cache")#禁用缓存
options.add_argument('disable-infobars')
options.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
browser = webdriver.Chrome(options=options)
browser.get(url)

cookies = browser.get_cookies()
savecookies(cookies)
print('cookie获取成功')
browser.quit()
