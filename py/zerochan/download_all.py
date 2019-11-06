import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import sys
import random
import os
import io
import time

url = "https://www.zerochan.net/"
tag = "kaito"

data_dir = "IMAGES/"

#proxies = { 'https' : 'https://user:password@proxyip:port' }
proxies = { 'https' : 'https://SVQt25:0sMxAn@45.4.199.164:8000',
            'http' : 'https://62.33.207.201:3128'}

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}

s = requests.session()

r = s.get(url + tag, proxies=proxies)

soup = BeautifulSoup(r.text, 'html.parser')
tmp = soup.find(class_="pagination")
tmp = re.sub(r'\s+', ' ', tmp.text) #лишние пробелы
tmp = tmp.split(" ")
n_pages = int(tmp[4])

offset = 101

for page in range(n_pages - offset):
    r = s.get(url + tag + "?p=" + str(page + offset), proxies=proxies)
    print(page + offset)
    with open("tmptmp.html","w", encoding="utf-8") as f:
        f.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    tmp = soup.find("ul", id="thumbs2")
    images = tmp.find_all("li")
    for i, t in enumerate(images):
        try:
            image_url = t.find("p").find("a").get("href")
            print(image_url)
            image = s.get(image_url, proxies=proxies)
            image_filename = os.path.split(image_url)
            image_filename = data_dir + str(i) + image_filename[1]
            with open(image_filename, "wb") as f:
                for chunk in image:
                    f.write(chunk)
        except Exception as e:
            pass
