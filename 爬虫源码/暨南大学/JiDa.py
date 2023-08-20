import requests
import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}
url = "https://xxxy.jnu.edu.cn/2023/0428/c27469a750965/page.htm"

# 发送 HTTP 请求获取页面内容
response = requests.get(url, headers = headers)
response.encoding = 'utf-8'
html_content = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")


log_path = 'format_JD.csv'
file = open(log_path, 'a+', encoding='utf-8', newline='')
csv_writer = csv.writer(file)
csv_writer.writerow([f'讲座标题', '报告人', '时间', '地点', "通知全文链接","通知发布时间", "通知内容", "报告人简介"])



# titles = soup.find("h4", class_ = "article-title")
# title = str(titles.string)
# title = title.strip()

publish_timess = soup.find("p", class_ = "article-small")
publish_times = publish_timess.text.strip()
pbs = re.split(r"发布时间：|来源：", publish_times)
pbs = [i.strip() for i in pbs if i.strip()]
publish_time = pbs[0]

contentss = soup.find("div", class_ = "article-content")
contents = contentss.text.strip()
# print(contents)
items = re.split(r"目：|内容简介：|报告人：|报告人简介：|间：|点：|热烈欢迎广大师生参加!", contents)

title =  items[1]
content = items[2]
speaker = items[3]

speaker_file = items[4]
n = len(speaker_file)
speaker_file = speaker_file[:n-3]

time = items[5]
n = len(time)
time = time[:n-3]

location = items[6]

# # 遍历讲座信息元素，并提取文字信息
# for href in hrefs:
#     response1 = requests.get(base + href, verify=False)
#     content = response1.text
#     soup1 = BeautifulSoup(content, "html.parser")

#     titles = soup1.find("h2")
#     title = str(titles.string)
#     title = title.strip()

#     itemss = soup1.find("p")
#     items = str(itemss.text.strip())
#     item = re.split(r"演讲人：|时间：|地点：|内容：", items)
#     item = [i.strip() for i in item if i.strip()]
#     speaker = item[0]
#     time = item[1]
#     location = item[2]
    
print("标题:", title)
print("通知发布时间:", publish_time)
print("演讲者:", speaker)
print("时间:", time)
print("地点:", location)
print("演讲者简介:", speaker_file)
print("演讲内容:", content)
print("-------------------")

# csv_writer.writerow([title, speaker, time, location])

#     # with open(log_path, "w", newline="") as format:
#     #     format.truncate()
# file.close()