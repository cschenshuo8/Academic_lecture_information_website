import requests
import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import os
from urllib.request import urlretrieve
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

columns = ["讲座标题", "报告人", "时间", "地点", "大学", "通知全文链接", "通知发布时间", "通知内容", "报告人简介"]
wrong = [64, 68, 83]
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_url(seminar):

    positions_begin = seminar.find("href=")
    positions_end = seminar.find(".htm")
    ret = seminar[(positions_begin + 8): (positions_end + 4)]
    return ret

#获取暨大信息科学院的所有学术讲座网址
def Is_need(url_str):

    url = url_str  # 学术报告讲座网页URL
    response = requests.get(url, headers = head)
    ret = []
    #print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        title = soup.find('div', attrs = {'class' : 'Container'}).find('h2')
        title_text = str(title.text)
        print(title_text)
        if ('讲座' in title_text):
            ret.append(url_str)
    return ret

#滚动所有列表
def get_all_list():
    ret = []
    for i in range(200):
        str_num = str(i + 370)
        url_str = 'https://www.cs.sjtu.edu.cn/NewNoticeDetail.aspx?id=' + str_num
        print(url_str)
        tmp = Is_need(url_str)
        for t in tmp:
            ret.append(t)
    df = pd.DataFrame({'url': ret})
    df.to_csv("url.csv")

#获取照片
def parse_page(url, index):
    if index in wrong:
        return None
    # 1.获取网页请求
    response = requests.get(url, headers = head)
    text = response.text
    # print text
    # 2.解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')
    #images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    article = soup.find("div",attrs = {"class" : "Container"})
    image = article.find("img")
    # print etree.tostring(img)
    # img.get('data-original')：get方法可以得到‘data-original’属性的值
    if (image == None):
        return None
    img_url = "https://www.cs.sjtu.edu.cn/" + image.get("src")
    response1 = requests.get(img_url, headers = head)
    if (response1.status_code == 200):
        img_name = str(index)
        img_suffix = os.path.splitext(img_url)[-1]
        img_filename = img_name+img_suffix
        print(img_filename)
        urlretrieve(img_url, "Images/"+img_filename, report_hook)
        return "Images/" + img_filename
    else:
        return None

def report_hook(a, b, c):
    """回调函数
    :param a:已经下载的数据块
    :param b:数据块的大小
    :param c:远程文件的大小
    :return:
    """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    #print("%.2f%%" % per)

#提取文字
def get_words(img, index):
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = img
    result = ocr.ocr(img_path, cls=True)
    result = result[0]

    # 显示结果
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    dataframe = pd.DataFrame({'box': boxes, 'txt': txts, 'score': scores})
    dataframe.to_csv("Images/" + str(index) + ".csv")

def get_graph(webs):
    cnt = 0
    for web in webs:
        print(web)
        img_path = parse_page(web, cnt)
        if (img_path != None):
            get_words(img_path, cnt)
        cnt += 1

def Is_match(text, all_key):
    for key in all_key:
        matchObj = re.search(key, text)
        if (matchObj != None):
            #print(matchObj.group())
            return True

    return False

def seize_from_graph(id, ret):
    if (os.access("Images/" + str(id) + ".csv", os.F_OK) == False):
        return ret
    df = pd.read_csv("Images/" + str(id) + ".csv")
    boxes = list(df['box'])
    txts = list(df['txt'])

    for i in range(len(txts)):
        txt = str(txts[i])

        #报告人
        reporter_key = ["Presenter.*", "Host.*", "Prof.*","报告人.?(\n)*.*", "主讲人.?(\n)*.*" , "Speaker.?(\n)*.*", ".*博士"]
        if (Is_match(txt, reporter_key) and ret[1] == None):
            ret[1] = txt

        #时间
        time_key = ["时间.?(\n)*.*", "Time.?(\n)*.*", ".*月.*日.*"]
        if (Is_match(txt, time_key) and ret[2] == None):
            ret[2] = txt

        #地点
        place_key = ["地点.?(\n)*.*", "Location.?(\n)*.*", "Venue.*", "参与方式.*"]
        if (Is_match(txt, place_key) and ret[3] == None):
            ret[3] = txt

        #通知内容
        abstract_key = ["Abstract.?(\n)*.*", "摘要.?(\n)*.*", "讲座简介.?(\n)*.*"]
        if (Is_match(txt, abstract_key) and ret[7] == None):
            ret[7] = ''
            for j in range(i, len(txts)):
                tmp = str(txts[j])
                if (tmp[-1] == '。' or tmp[-1] == '.'):
                    break
                ret[7] += tmp
            print(ret[7])

        #报告人简介
        reporter_introduction_key = ['专家简介.?(\n)*.*', "Biography.?(\n)*.*", "教授简介.?(\n)*.*", "Bio:(\n)*.*"]
        if (Is_match(txt, reporter_introduction_key) and ret[8] == None):
            ret[8] = ''
            for j in range(i, len(txts)):
                tmp = str(txts[j])
                if (tmp[-1] == '。' or tmp[-1] == '.'):
                    break
                ret[8] += tmp

    print(ret)
    return ret

def prase_info(url, id):
    ret = []
    response = requests.get(url, headers=head)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    #讲座标题
    #print(type(article_text))
    title = soup.find('div', attrs={'class': 'Container'}).find('h2')
    title_text = str(title.text)
    ret.append(title_text)

    #报告人
    ret.append(None)

    #时间
    ret.append(None)

    #地点
    ret.append(None)

    #大学
    ret.append("上海交通大学")

    #通知全文链接
    ret.append(url)

    #通知发布时间
    publish_time = soup.find("div", attrs = {"class" : "tc lh300"}).text
    ret.append(str(publish_time))

    #通知内容
    ret.append(None)

    #报告人简介
    ret.append(None)

    #print(ret)
    ret = seize_from_graph(id, ret)
    if (ret[2] == None):
        ret[2] = ret[6]
    if (ret[8] == None):
        ret[8] = ret[1]
    print(ret)
    return ret

def get_info(webs):
    info = []
    cnt = 0
    for web in webs:
        tmp = prase_info(web, cnt)
        info.append(tmp)
        cnt += 1

    df = pd.DataFrame(data = info , columns = columns)
    df.to_csv('data.csv')

#get_all_list()
df = pd.read_csv("url.csv")
webs = list(df['url'])
#get_graph(webs)
get_info(webs)
#prase_info("https://eecs.pku.edu.cn/info/1050/2100.htm")