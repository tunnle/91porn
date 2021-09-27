import requests
import random
import os


cookie=""

with open(os.getcwd()+"\\url.txt", "r",encoding='utf-8') as urls:
    for url in urls.readlines():
        print(url)
        cookies = requests.cookies.RequestsCookieJar()
        cookies.set("language", "cn_CN", domain=".p06.rocks", path="/")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',"Accept-Language":"zh-CN,zh;","Cookie":cookie}
        try:
            response=requests.get(url,headers=headers,timeout=15)
        except requests.exceptions.RequestException:
            pass
        with open(os.getcwd()+"\\temp.txt","w",encoding='utf-8') as f:
            f.write(response.text)
        with open(os.getcwd()+"\\temp.txt", "r",encoding='utf-8') as f:
            for line in f.readlines():
                if line.find('<title> ')==-1:
                    pass
                else:  
                    title=line.replace('<title>','').replace(' ','')                  
                if line.find('<div id=VID style="display:none;">')==-1:
                    pass
                else:
                    m3u8=line.replace('<div id=VID style="display:none;">','').replace('</div>','').replace(" ","").replace('\t','').strip()
                    m3u8url='https://ccn.killcovid2021.com/m3u8/'+m3u8+'/'+m3u8+'.m3u8'
                    with open(os.getcwd()+"\\m3u8url.txt","a",encoding='utf-8') as f:
                        f.write(m3u8url+','+title)
    print("所有视频下载地址获取完成，接下来开始下载")
    os.system(os.getcwd()+'\\M3U8Downloader.exe')