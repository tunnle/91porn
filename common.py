# -*- coding: UTF-8 -*-
import requests, re, time, random, threading,os
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


cookie=''
with open(os.getcwd() + '\cookies.txt', 'r', encoding='utf-8') as f:
    cookie = f.read().replace('[','').replace(']','')

#--------------------------------------
# 91 的临时站点，可以随时更换
#URL = "http://91porn.com/"
#URL = "http://91.91p17.space/"
#URL = "https://p06.rocks"
# 用HTTP协议
URL = "http://91porn.com/"
#----------------------------------------
import os


'''
  获取访问的主页面
'''
def getNumber():
    r = 0
    while True:
        num = input("请输入想爬的页数:")
        try:
            r = int(num)
            break
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue
    return r

def visit(url):
    retries = Retry(total=5,backoff_factor=10, status_forcelist=[500,502,503,504])
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'Host':'807.workgreat17.live',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=retries))
    html = s.get(url, headers=headers, stream=True).content
    return html
