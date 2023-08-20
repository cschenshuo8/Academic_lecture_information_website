import requests
import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

webs = []
with open('website_ZD.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]  # 假设网址在第一列
        if url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url  # 添加模式
            webs.append(url)

print(webs)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
}


log_path = 'format_ZD.csv'
file = open(log_path, 'a+', encoding='utf-8', newline='')
with open(log_path, "w", newline="") as format:
        format.truncate()
csv_writer = csv.writer(file)
csv_writer.writerow([f'讲座标题', '报告人', '时间', '地点', '大学', "通知全文链接","通知发布时间", "通知内容", "报告人简介"])

for web in webs:

    # 发送 HTTP 请求获取页面内容
    response = requests.get(web, headers = headers)
    response.encoding = 'utf-8'
    html_content = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")

    def seize_from_key(text, all_key):
        f = 0
        for key in all_key:
            matchObj = re.search(key, text)
            if (matchObj != None):
                #print(matchObj.group())
                return matchObj.group()
                f = 1
                break
            #else:
                #print("None")

        if (f == 0):
            return None


    articles = soup.find("td", attrs={"class": "nrhei"})
    article = str(articles.text)

    #讲座标题
    title_key = ["演讲：(\n)*.*", "Topic.(\n)*.*", "主题.(\n)*.*", "题目.(\n)*.*"]
    title = seize_from_key(article, title_key)
    if (title == None):
            titles = soup.find("td", attrs={"class":"lan_15"})
            title = titles.text
    items = re.split(r"演讲：|Topic:|主题：|题目：", str(title))
    if len(items) > 1:
        title = items[1]


    #报告人
    reporter_key = ["报告人.?(\n)*.*", "主讲人.?(\n)*.*", "Speaker.?(\n)*.*", ".*博士"]
    speaker = seize_from_key(article, reporter_key)
    items = re.split(r"报告人：|主讲人：|Speaker:", str(speaker))
    if len(items) > 1:
        speaker = items[1]

    #时间
    time_key = ["时间.?(\n)*.*", "Time.?(\n)*.*", ".*月.*日.*"]
    time = seize_from_key(article, time_key)
    items = re.split(r"时间：", str(time))
    if len(items) > 1:
        time = items[1]


    #地点
    place_key = ["地点.?(\n)*.*", "Location.?(\n)*.*", ".*厅"]
    location = seize_from_key(article, place_key)
    items = re.split(r"地点：", str(location))
    if len(items) > 1:
        location = items[1]


    #通知全文链接

    #通知内容
    abstract_key = ["Abstract.?(\n)*.*", "摘要.?(\n)*.*", "讲座简介.?(\n)*.*", "报告简介.?(\n)*.*", "讲座概要.?(\n)*.*", "内容简介.?(\n)*.*"]
    content = seize_from_key(article, abstract_key)
    items = re.split(r"Abstract:|摘要：|讲座简介：|报告简介：|讲座概要：|内容简介：", str(content))
    if len(items) > 1:
        content = items[1]

    #报告人简介
    reporter_introduction_key = ['专家简介.?(\n)*.*',"Biography.?(\n)*.*", "教授简介.?(\n)*.*", "报告人简介.?(\n)*.*", "主讲人介绍.?(\n)*.*", "个人简介.?(\n)*.*"]
    speaker_file = seize_from_key(article, reporter_introduction_key)
    items = re.split(r"专家简介：| Biography:|教授简介：|报告人简介：|主讲人介绍：|个人简介：", str(speaker_file))
    if len(items) > 1:
        speaker_file = items[1]

    #发布时间
    publish_time = ""



    print("标题:", title)
    print("通知发布时间:", publish_time)
    print("演讲者:", speaker)
    print("时间:", time)
    print("地点:", location)
    print("演讲者简介:", speaker_file)
    print("演讲内容:", content)
    print("web:", web)
    print("-------------------")



    csv_writer.writerow([title, speaker, time, location, "信息安全国家重点实验室", web, publish_time, content, speaker_file])

file.close()