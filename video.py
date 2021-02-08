# -*- coding = utf-8 -*-
# @Time: 2021/2/8 13:41
# @Author: DELL
# @Site: 
# @File: video.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
}
response = requests.get("https://zztt09.com/archives.html", headers=headers)
html = response.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all("div", class_="brick")
# print(divs)
# videos = []
htmls = []
for div in divs:
    href = div.find_all("a")[0]
    # print(href)
    # name = href.text
    url = href["href"]
    # name = name.replace("\n", "")
    # path = name + '({})'.format(url)
    # print(path)
    # print(name)
    # videos.append(path)
    htmls.append(url)
# print(videos)
# with open("video.txt", "w", encoding='utf-8') as f:
#     for url in videos:
#         f.write(url)
#         f.write("\n")
#     f.close()
# print(htmls)
# video_url = []
with open("video.txt", "w", encoding="utf-8") as f:
    for child_url in htmls:
        child_html = requests.get(child_url, headers=headers).text
        soup = BeautifulSoup(child_html, "html.parser")
        title = soup.find_all("h1")
        divs = soup.find_all("div", class_="dplayer")
        print(title[0].text)
        f.write(title[0].text)
        f.write("\n")
        if divs:
            data = divs[0]["data-config"]
        # print(data)
        load_data = json.loads(data)
        url = load_data.get("video").get("url")
        f.write(url)
        f.write("\n")
        print(url)
        # video_url.append(url)
        # print(divs[0])
    print("保存成功")
    f.close()
