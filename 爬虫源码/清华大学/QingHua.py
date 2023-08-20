import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




base = "https://iiis.tsinghua.edu.cn/show-10390-1.html"

log_path = 'format_QH.csv'
file = open(log_path, 'a+', encoding='utf-8', newline='')
with open(log_path, "w", newline="") as format:
        format.truncate()
csv_writer = csv.writer(file)
csv_writer.writerow([f'讲座标题', '报告人', '时间', '地点', '通知全文链接', "通知内容", "报告人简介"])

# 遍历讲座信息元素，并提取文字信息

web = base
response = requests.get(web, verify=False)
response.encoding = 'utf-8'
content = response.text
soup = BeautifulSoup(content, "html.parser")

titles = soup.find("h2")
title = str(titles.string)
title = title.strip()


# 使用选择器选择所有符合条件的标签
# p_tags = soup.select('p[style="text-align: justify;"]')

# for p in p_tags:
#         print(p)
# 提取每个标签的文字内容
# contents_tag = p_tags[0]
# contents = contents_tag.get_text(strip=True)
# speaker_file = ""
# for p_tag in p_tags:
#     if p_tag != contents_tag:
#           text = p_tag.get_text(strip=True)
#           speaker_file += text


itemss = soup.find("div", class_ = "news_info qh_desc2")
items = str(itemss.text.strip())

item = re.split(r"演讲人：|时间：|地点：|内容：|个人简介:", items)
item = [i.strip() for i in item if i.strip()]
speaker = item[0]
time = item[1]
location = item[2]
contents = item[3]
speaker_file = item[4]

print("标题:", title)
print("演讲者:", speaker)
print("时间:", time)
print("地点:", location)
print("web:", web)
print("通知内容:", contents)
print("报告人简介:", speaker_file)


print("-------------------")

csv_writer.writerow([title, speaker, time, location, web, contents, speaker_file])

with open(log_path, "w", newline="") as format:
    format.truncate()
file.close()
