# -*- coding = utf-8 -*-
# @Time: 2021/2/9 10:07
# @Author: DELL
# @Site: 
# @File: download.py
# @Software: PyCharm
import requests
import re


def m3u8(name, url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }
    # requests得到m3u8文件内容
    content = requests.get(url, headers=header).text
    if "#EXTM3U" not in content:
        print("这不是一个m3u8的视频链接！")
        return False

    # 得到每一个ts视频链接
    tslist = re.findall('EXTINF:(.*),\n(.*)\n#', content)
    newlist = []
    for i in tslist:
        newlist.append(i[1])

    # 先获取URL/后的后缀，再替换为空
    urlkey = url.split('/')[-1]
    url2 = url.replace(urlkey, '')  # 这里为得到url地址的前面部分，为后面key的链接和视频链接拼接使用

    # 得到每一个完整视频的链接地址
    tslisturl = []
    for i in newlist:
        tsurl = url2 + i
        tslisturl.append(tsurl)

    # for循环获取视频文件
    for i in tslisturl:
        res = requests.get(i, header)
        # 以追加的形式保存为mp4文件
        with open(name + '.mp4', 'ab+') as f:
            f.write(res.content)
    return True


if __name__ == '__main__':
    # f = open('video.txt', encoding='utf-8')
    # data = f.readlines()
    # # print(data)
    # video_name = []
    # video_url = []
    # for index in range(len(data)):
    #     if index % 2 == 0:
    #         video_name.append(data[index].replace("\n", ""))
    #     else:
    #         video_url.append(data[index].replace("\n", ""))
    # # print(video_name)
    # # print(video_url)
    # for position in range(len(video_name)):
    #     pd = m3u8(video_name[position], video_url[position])
    #     if pd:
    #         print('视频下载完成！')
    # print('下载完成！')
    pd = m3u8('这种身材你出多少钱？', "https://v.muyuanwy.com/public/videos/5f27bced85d78d3817493313/index.m3u8")
    if pd:
        print('视频下载完成！')