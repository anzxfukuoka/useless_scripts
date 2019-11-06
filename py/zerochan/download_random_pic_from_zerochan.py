import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import sys
import random
import os

url = "https://www.zerochan.net/"
tag = "kaito"

#proxies = { 'https' : 'https://user:password@proxyip:port' }
proxies = { 'https' : 'https://104.248.53.46:3128',
            'http' : 'https://104.248.53.46:3128'}

ua = UserAgent()
header = {'User-Agent':str(ua.random)}

s = requests.session()

r = s.get(url + tag, proxies=proxies)

soup = BeautifulSoup(r.text, 'html.parser')
tmp = soup.find(class_="pagination")
tmp = re.sub(r'\s+', ' ', tmp.text) #лишние пробелы
tmp = tmp.split(" ")
n_pages = int(tmp[4])

page = random.randint(1, n_pages)
print("page: ", page)

r = s.get(url + tag, proxies=proxies, data={'p': page})

soup = BeautifulSoup(r.text, 'html.parser')
tmp = soup.find("ul", id="thumbs2")
images = tmp.find_all("li")
for i, t in enumerate(images):
    images[i] = t.find("p").find("a").get("href")

i = random.randint(0, len(images) - 1)
image_url = images[i]
image = s.get(image_url, proxies=proxies)


image_filename = os.path.split(image_url)
image_filename = image_filename[1]

with open(image_filename, "wb") as f:
    for chunk in image:
        f.write(chunk)
