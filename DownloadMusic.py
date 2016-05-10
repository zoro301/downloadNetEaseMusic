#coding:utf-8


import requests
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

r = requests.get('http://music.163.com/api/playlist/detail?id=19723756')	# 云音乐飙升榜

result = r.json()['result']['tracks']
for i in range(50):	
		name = str(i+1) + ' ' + result[i]['name'] + '.mp3'
		link = result[i]['mp3Url']
#文件下载后的存储位置，包含文件名。这里注意两点，该方法为python2.x提供，若使用python3.x，方法修改为urllib.request.urlretrieve。第二文件名后的分隔符‘/’,是linux的，使用windows形式的“\\”会被作为普通字符串处理。
		urllib.urlretrieve(link, 'music/' + name)
		print(name + ' 下载完成.')
