# -*- coding: UTF-8 -*-
import requests, re, time, random, threading
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import common
from bs4 import BeautifulSoup
import os

def parseList(url):
    m = common.visit(url)
    soup = BeautifulSoup(m,'html.parser')
    for url in soup.findAll('a'):
        lst = url.get('href')
        with open(os.getcwd()+"\\url.txt","a") as f1:
                if lst.find('http://807.workgreat17.live/view_video.php?viewkey=')!=-1:
                    print(lst)
                    f1.writelines(lst+"\n")

'''
    线程主方法
'''
def enter(**kwargs):
    start = kwargs["start"]
    end = kwargs["end"]
    for page in range(start, end):
        url = common.URL + "/v.php?category=rf&viewtype=basic&page=" + str(page)
        try:
            print(threading.current_thread().name, " 解析 ", page, " 页 ", url)
            parseList(url)
            time.sleep(random.randint(1, 3))
        except RuntimeError:
            print(threading.current_thread().name, " visiting page ", page, " occurs some errors ", RuntimeError.__with_traceback__)
            continue

def start():
    thread_list = []
    total = common.getNumber()
    thread_total = 5 

    if total <= 5:
        page_size = 1
        thread_total = total
    else:
        page_size = int(total / 5) 

    for i in range(1, thread_total + 1):
        start = (i - 1) * page_size + 1
        end = i * page_size + 1
        name = "a" + str(i)
        t = threading.Thread(target=enter, name=name, kwargs={"start":start,"end":end})
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print("网页解析完毕,下一步请运行downloadm3u8.py")
