import requests
import random
import os

cookie=''
with open(os.getcwd() + '\cookies.txt', 'r', encoding='utf-8') as f:
    cookie = f.read().replace('[','').replace(']','')
with open(os.getcwd()+"\\url.txt", "r",encoding='utf-8') as urls:
    for url in urls.readlines():
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,pl;q=0.4',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':cookie,
            'Host':'91porn.com',
            'Referer':'http://91porn.com/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
            }
        try:
            response=requests.get(url,headers=headers,timeout=15)
            with open(os.getcwd()+"\\temp.txt","a",encoding='utf-8') as f:
                f.write(response.text)
        except requests.exceptions.RequestException as e:
            print(e)
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
                    m3u8url='https://la.killcovid2021.com//m3u8/'+m3u8+'/'+m3u8+'.m3u8'
                    with open(os.getcwd()+"\\m3u8url.txt","a",encoding='utf-8') as f:
                        f.write(m3u8url+','+title)
                        print(title)
        with open(os.getcwd()+"\\temp.txt","w",encoding='utf-8') as f:
            f.write('')
    print("所有视频下载地址获取完成，接下来开始下载")
    os.system(os.getcwd()+'\\M3U8Downloader.exe')
