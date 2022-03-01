#好像又能用了（2022-03-01）
# 91porn
91pron爬虫

自行通过pip install selenium安装所需的库。脚本基于chrome开发，电脑必须安装chrome浏览器并且需要自己下载正确的驱动，下载所需的驱动exe文件请访问http://chromedriver.storage.googleapis.com/index.html 下载好自己浏览器版本对应的驱动并放到脚本同一目录即可。如果想实现完全自动化请参考common.py第35行的备注简单修改即可，目前的设置需要手动输入一次自己想爬的页数




使用方式：
1.下载所有的py文件还有m3u8downloader解压后放在同一个文件夹内。
2.双击  运行.bat ，根据提示输入想要抓取的页数（确保自己能访问91的网址，网址在common.py的第16行）
3.等待网页抓取完成，抓取完成后会自动调用exe下载视频。




文件结构参考（打叉的几个请无视）
![image](https://user-images.githubusercontent.com/18001712/141744716-2e135d87-5636-44cc-8c9d-139d9b6c9447.png)

下载器和脚本要在同一个文件夹里才能全自动下载，不支持设置下载路径，默认路径为当前文件夹下的Videos文件夹，这个文件夹会自动生成
