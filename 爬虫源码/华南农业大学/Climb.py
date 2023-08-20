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
def fetch_website_list(url_str):

    url = url_str  # 学术报告讲座网页URL
    response = requests.get(url, headers = head)
    ret = []
    #print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        all_list_ul = soup.find_all('ul', attrs = {"class": "list-text"})
        for list_ul in all_list_ul:
            all_link = list_ul.find_all('a')
            for link in all_link:
                link1 = get_url(str(link))
                ret.append('https://eecs.pku.edu.cn' + link1)
    return ret

#滚动所有列表
def get_all_list():
    ret = []
    for i in range(11):
        if i == 0:
            str_num = ''
        else:
            str_num = '/' + str(i)
        url_str = 'https://eecs.pku.edu.cn/index/jzxx' + str_num + '.htm'
        #print(url_str)
        tmp = fetch_website_list(url_str)
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
    article = soup.find("div",attrs = {"class" : "article-text"})
    image = article.find("img")
    # print etree.tostring(img)
    # img.get('data-original')：get方法可以得到‘data-original’属性的值
    if (image == None):
        return None
    img_url = "https://eecs.pku.edu.cn/" + image.get("src")
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


def seize_from_graph(id, graph_id, ret):
    if (os.access("Images/" + str(id) + ".csv", os.F_OK) == False):
        return ret
    df = pd.read_csv("Images/" + str(id) + ".csv")
    boxes = list(df['box'])
    txts = list(df['txt'])

    if (graph_id == 1):
        # 讲座标题
        while ('知存讲座' not in txts[0]):
            txts.pop(0)
            boxes.pop(0)
        while ('知存讲座' in txts[0]):
            txts.pop(0)
            boxes.pop(0)
        if ('时间' not in txts[0]):
            ret[0] = txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 时间
        if ('时间' in txts[0]):
            ret[2] = txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 地点
        if ('地点' in txts[0]):
            ret[3] = txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 除去多余的文字
        txts_tmp = []
        boxes_tmp = []
        for i in range(len(txts)):
            num_list = re.findall(r"[-+]?\d+\.?\d*[eE]?[-+]?\d*", boxes[i])

            if (float(num_list[3]) / float(num_list[4]) < 5.0):
                txts_tmp.append(txts[i])
                boxes_tmp.append(boxes[i])
        txts = txts_tmp
        boxes = boxes_tmp

        # 报告人
        ret[1] = txts[0]
        txts.pop(0)
        boxes.pop(0)

        # 报告人简介
        ret[8] = txts[0]
        txts.pop(0)
        boxes.pop(0)

        # 通知内容
        ret[7] = ''
        while (len(txts) != 0):
            ret[7] = ret[7] + str(txts[0])
            txts.pop(0)
            boxes.pop(0)

    if (graph_id == 2):
        # 讲座标题
        while (re.search('第.*期', txts[0]) == None):
            txts.pop(0)
            boxes.pop(0)
        txts.pop(0)
        boxes.pop(0)
        ret[0] = ''
        while ('时间' not in txts[0]):
            ret[0] += txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 文字分组
        txts_left = []
        txts_right = []
        boxes_left = []
        boxes_right = []
        for i in range(len(txts)):
            num_list = re.findall(r"[-+]?\d+\.?\d*[eE]?[-+]?\d*", boxes[i])
            if (float(num_list[0]) < 300.0):
                txts_left.append(txts[i])
                boxes_left.append(boxes[i])
            else:
                txts_right.append(txts[i])
                boxes_right.append(boxes[i])

        # 报告人
        ret[1] = txts_left[0]
        txts_left.pop(0)
        boxes_left.pop(0)

        # 时间
        ret[2] = ''
        while ('地点' not in txts_right[0]):
            ret[2] += txts_right[0]
            txts_right.pop(0)
            boxes_right.pop(0)

        # 地点
        ret[3] = ''
        while (len(txts_right) > 0):
            ret[3] += txts_right[0]
            txts_right.pop(0)
            boxes_right.pop(0)

        # 报告人简介
        ret[8] = ''
        while (len(txts_left) > 0):
            ret[8] += txts_left[0]
            txts_left.pop(0)
            boxes_left.pop(0)

    if (graph_id == 3):
        # 讲座标题
        while (re.search('第.*期', txts[0]) == None):
            txts.pop(0)
            boxes.pop(0)
        txts.pop(0)
        boxes.pop(0)
        ret[0] = txts[0]
        txts.pop(0)
        boxes.pop(0)

        # 报告人
        ret[1] = ''
        while ('时间' not in txts[0]):
            ret[1] += txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 时间
        ret[2] = txts[0]
        txts.pop(0)
        boxes.pop(0)

        # 地点
        ret[3] = txts[0]
        txts.pop(0)
        boxes.pop(0)

        # 通知内容
        while ('报告摘要' not in txts[0]):
            txts.pop(0)
            boxes.pop(0)
        txts.pop(0)
        boxes.pop(0)
        ret[7] = ''
        while ('报告人简介' not in txts[0]):
            ret[7] += txts[0]
            txts.pop(0)
            boxes.pop(0)

        # 报告人简介
        txts.pop(0)
        boxes.pop(0)
        ret[8] = ''
        while (len(txts) > 0):
            ret[8] += txts[0]
            txts.pop(0)
            boxes.pop(0)
    return ret

def seize_from_key(text, all_key, id):
    f = 0
    for key in all_key:
        matchObj = re.search(key, text)
        if (matchObj != None):
            #print(matchObj.group())
            return matchObj.group()
            f = 1
            break

    if (f == 0):
        return None

def prase_info(url, id):
    ret = []
    response = requests.get(url, headers=head)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find("div", attrs = {"class": "row"}).find("div",attrs = {"class": "wp_articlecontent"}).find_all("p")

    article_text = ""
    for para in article:
        para_text = str(para)
        para_text = para_text.replace("<br/>", "\n")
        para_text = re.sub("<[^>]+>", "", para_text)
        article_text += para_text + "\n"
        #print(para)
    #print(article_text)

    #讲座标题
    title_text = soup.find("h3").text
    if ('报告' not in title_text):
        return ret
    ret.append(title_text)

    #报告人
    reporter_key = ["报告人.?(\n)*.*", "主讲人.?(\n)*.*" , "Speaker.?(\n)*.*"]
    ret.append(seize_from_key(article_text, reporter_key, id))

    #时间
    time_key = ["日期.?(\n)*.*\n时间.*","时间.?(\n)*.*", "Time.?(\n)*.*", ".*月.*日.*"]
    ret.append(seize_from_key(article_text, time_key, id))

    #地点
    place_key = ["地点.?(\n)*.*", "Location.?(\n)*.*","#腾讯会议.?(\n)*.*","腾讯会议号.?(\n)*.*","腾讯会议ID.?(\n)*.*","线上报告.?(\n)*.*"]
    ret.append(seize_from_key(article_text, place_key, id))

    #大学
    ret.append("华南农业大学")

    #通知全文链接
    ret.append(url)

    #通知发布时间
    publish_time = soup.find("small").find("span").text
    ret.append(str(publish_time))

    #通知内容
    abstract_key = ["Abstract.?(\n)*.*", "摘要.?(\n)*.*", "摘  要.?(\n)*.*", "讲座简介.?(\n)*.*","报告内容.?(\n)*.*","报告简介.?(\n)*.*"]
    ret.append(seize_from_key(article_text, abstract_key, id))

    #报告人简介
    reporter_introduction_key = ['报告人简介.?(\n)*.*','专家简介.?(\n)*.*',"Biography.?(\n)*.*", "教授简介.?(\n)*.*", "个人简介.?(\n)*.*","报告人介绍.?(\n)*.*", "报告嘉宾简介.?(\n)*.*"]
    ret.append(seize_from_key(article_text, reporter_introduction_key, id))

    if (ret[2] == None):
        ret[2] = ret[6]

    print(ret[8])
    print(ret[5])
    return ret

def get_info(webs):
    info = []
    cnt = 0
    for web in webs:
        tmp = prase_info(web, cnt)
        if (len(tmp) != 0):
            info.append(tmp)
        cnt += 1

    df = pd.DataFrame(data = info , columns = columns)
    df.to_csv('data.csv')

#get_all_list()
df = pd.read_csv("url.csv")
webs = list(df['url'])
#get_graph(webs)
get_info(webs)
#prase_info("https://info.scau.edu.cn/2022/0505/c12892a314103/page.htm",1)