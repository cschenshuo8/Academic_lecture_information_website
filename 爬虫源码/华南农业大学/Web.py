import requests
import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_url(seminar):

    positions_begin = seminar.find("href=")
    positions_end = seminar.find("page.htm")
    ret = seminar[(positions_begin + 6): (positions_end + 8)]
    return ret

#获取暨大信息科学院的所有学术讲座网址
def fetch_website_list(url_str):
    head = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }
    url = url_str  # 学术报告讲座网页URL
    response = requests.get(url, headers = head)
    ret = []
    #print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        all_list_ul = soup.find_all('a', attrs = {"class": "stretched-link"})
        for list_ul in all_list_ul:
            link1 = get_url(str(list_ul))
            ret.append('https://info.scau.edu.cn' + link1)
    return ret

#滚动所有列表
def get_all_list():
    ret = []
    for i in range(3):
        url_str = 'https://info.scau.edu.cn/xsdt/list' + str(i) + '.htm'
        tmp = fetch_website_list(url_str)
        for t in tmp:
            ret.append(t)
    df = pd.DataFrame({'url': ret})
    df.to_csv("url.csv")

get_all_list()