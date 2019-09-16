import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://www.xjistedu.cn/")
r.encoding = r.apparent_encoding

soup = bs(r.text)
for trr in soup.findAll('div',{'class':'wrapper'}):
    print("class标签描述" +trr.text)