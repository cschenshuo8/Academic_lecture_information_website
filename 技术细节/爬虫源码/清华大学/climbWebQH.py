import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# def get_url(seminar):

#     positions_begin = seminar.find("href=")
#     positions_end = seminar.find(".html")
#     ret = seminar[(positions_begin + 6): (positions_end + 5)]
#     return ret

# #获取暨大信息科学院的所有学术讲座网址
# def fetch_website_list(url_str):
#     head = {
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
#     }
#     url = url_str  # 学术报告讲座网页URL
#     response = requests.get(url, headers = head, verify=False)
#     ret = []
#     #print(response.text)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         #print(soup)
#         all_list_ul = soup.find_all('div', attrs = {"class": "list_jzuo"})
#         for list_ul in all_list_ul:
#             all_link = list_ul.find_all('a')
#             for link in all_link:
#                 link1 = get_url(str(link))
#                 ret.append('https://iiis.tsinghua.edu.cn' + link1)
#     return ret

# #滚动所有列表
# def get_all_list():
#     ret = []
#     for i in range(10):
#         url_str = 'https://iiis.tsinghua.edu.cn/list-265-' + str(i) + '.html'
#         tmp = fetch_website_list(url_str)
#         for t in tmp: 
#             ret.append(t)
#             print(t)
#     return ret

# ret = get_all_list()
# print(ret)

# webs = ret


webs = []
with open('websiteQH.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]  # 假设网址在第一列
        if url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url  # 添加模式
            webs.append(url)

print(webs)



log_path = 'format_QH.csv'
file = open(log_path, 'a+', encoding='utf-8', newline='')
with open(log_path, "w", newline="") as format:
        format.truncate()
csv_writer = csv.writer(file)
csv_writer.writerow([f'讲座标题', '报告人', '时间', '地点', '大学', '通知全文链接',"通知内容", "报告人简介"])

# 遍历讲座信息元素，并提取文字信息
for web in webs:

    print(web)

    response = requests.get(web, verify=False)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find("h2")
    title = str(titles.string)
    title = title.strip()


    itemss = soup.find("div", class_ = "news_info qh_desc2")
    items = str(itemss.text.strip())

    item = re.split(r"演讲人：|时间：|地点：|内容：|个人简介:", items)
    item = [i.strip() for i in item if i.strip()]
    speaker = item[0]
    time = item[1]
    location = item[2]
    contents = item[3]
    if len(item) == 4:
         speaker_file = "None"
    else:
         speaker_file = item[4]

    print("标题:", title)
    print("演讲者:", speaker)
    print("时间:", time)
    print("地点:", location)
    print("web:", web)
    print("通知内容:", contents)
    print("报告人简介:", speaker_file)


    print("-------------------")


    csv_writer.writerow([title, speaker, time, location, "清华大学", web, contents, speaker_file])

file.close()
