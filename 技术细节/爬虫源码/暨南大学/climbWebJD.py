import requests
import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# def get_url(seminar):

#     positions_begin = seminar.find("href=")
#     positions_end = seminar.find("page.htm")
#     ret = seminar[(positions_begin + 6): (positions_end + 8)]
#     return ret

# #获取暨大信息科学院的所有学术讲座网址
# def fetch_website_list(url_str):
#     head = {
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
#     }
#     url = url_str  # 学术报告讲座网页URL
#     response = requests.get(url, headers = head)
#     ret = []
#     #print(response.text)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         #print(soup)
#         all_list_ul = soup.find_all('ul', attrs = {"class": "list-ul"})
#         for list_ul in all_list_ul:
#             all_link = list_ul.find_all('a')
#             for link in all_link:
#                 if "讲座" in link.text:
#                     link1 = get_url(str(link))
#                     ret.append('https://xxxy.jnu.edu.cn' + link1)
#     return ret

# #滚动所有列表
# def get_all_list():
#     ret = []
#     for i in range(40):
#         url_str = 'https://xxxy.jnu.edu.cn/27469/list' + str(i) + '.htm'
#         tmp = fetch_website_list(url_str)
#         for t in tmp:
#             ret.append(t)
#     return ret

# webs = get_all_list()
# print(webs)


webs = ['https://xxxy.jnu.edu.cn/2023/0428/c27469a750965/page.htm', 'https://xxxy.jnu.edu.cn/2023/0426/c27469a746099/page.htm', 'https://xxxy.jnu.edu.cn/2023/0413/c27469a743995/page.htm', 'https://xxxy.jnu.edu.cn/2023/0412/c27469a743879/page.htm', 'https://xxxy.jnu.edu.cn/2023/0412/c27469a743759/page.htm', 'https://xxxy.jnu.edu.cn/2023/0410/c27469a743155/page.htm', 'https://xxxy.jnu.edu.cn/2023/0331/c27469a741913/page.htm', 'https://xxxy.jnu.edu.cn/2023/0328/c27469a741305/page.htm', 'https://xxxy.jnu.edu.cn/2023/0322/c27469a740343/page.htm', 'https://xxxy.jnu.edu.cn/2023/0317/c27469a739581/page.htm', 'https://xxxy.jnu.edu.cn/2023/0314/c27469a739049/page.htm', 'https://xxxy.jnu.edu.cn/2023/0223/c27469a736397/page.htm', 'https://xxxy.jnu.edu.cn/2022/1212/c27469a732497/page.htm', 'https://xxxy.jnu.edu.cn/2022/1206/c27469a731541/page.htm', 'https://xxxy.jnu.edu.cn/2022/1201/c27469a730921/page.htm', 'https://xxxy.jnu.edu.cn/2022/1127/c27469a730395/page.htm', 'https://xxxy.jnu.edu.cn/2022/1122/c27469a729419/page.htm', 'https://xxxy.jnu.edu.cn/2022/1117/c27469a728285/page.htm', 'https://xxxy.jnu.edu.cn/2022/1110/c27469a727023/page.htm', 'https://xxxy.jnu.edu.cn/2022/1108/c27469a726407/page.htm', 'https://xxxy.jnu.edu.cn/2022/1101/c27469a724881/page.htm', 'https://xxxy.jnu.edu.cn/2022/1027/c27469a724033/page.htm', 'https://xxxy.jnu.edu.cn/2022/1021/c27469a723223/page.htm', 'https://xxxy.jnu.edu.cn/2022/1014/c27469a722283/page.htm', 'https://xxxy.jnu.edu.cn/2022/1011/c27469a721725/page.htm', 'https://xxxy.jnu.edu.cn/2022/1010/c27469a721539/page.htm', 'https://xxxy.jnu.edu.cn/2022/1008/c27469a721155/page.htm', 'https://xxxy.jnu.edu.cn/2022/0919/c27469a718475/page.htm', 'https://xxxy.jnu.edu.cn/2022/0916/c27469a718047/page.htm', 'https://xxxy.jnu.edu.cn/2022/0915/c27469a717819/page.htm', 'https://xxxy.jnu.edu.cn/2022/0629/c27469a707899/page.htm', 'https://xxxy.jnu.edu.cn/2022/0624/c27469a707209/page.htm', 'https://xxxy.jnu.edu.cn/2022/0617/c27469a705975/page.htm', 'https://xxxy.jnu.edu.cn/2022/0613/c27469a705113/page.htm', 'https://xxxy.jnu.edu.cn/2022/0610/c27469a704675/page.htm', 'https://xxxy.jnu.edu.cn/2022/0607/c27469a703773/page.htm', 'https://xxxy.jnu.edu.cn/2022/0606/c27469a703635/page.htm', 'https://xxxy.jnu.edu.cn/2022/0601/c27469a702837/page.htm', 'https://xxxy.jnu.edu.cn/2022/0530/c27469a702601/page.htm', 'https://xxxy.jnu.edu.cn/2022/0530/c27469a702317/page.htm', 'https://xxxy.jnu.edu.cn/2022/0523/c27469a700845/page.htm', 'https://xxxy.jnu.edu.cn/2022/0523/c27469a700825/page.htm', 'https://xxxy.jnu.edu.cn/2022/0518/c27469a700011/page.htm', 'https://xxxy.jnu.edu.cn/2022/0518/c27469a699607/page.htm', 'https://xxxy.jnu.edu.cn/2022/0517/c27469a699521/page.htm', 'https://xxxy.jnu.edu.cn/2022/0513/c27469a698959/page.htm', 'https://xxxy.jnu.edu.cn/2022/0510/c27469a696309/page.htm', 'https://xxxy.jnu.edu.cn/2022/0507/c27469a695545/page.htm', 'https://xxxy.jnu.edu.cn/2022/0505/c27469a695209/page.htm', 'https://xxxy.jnu.edu.cn/2022/0505/c27469a695085/page.htm', 'https://xxxy.jnu.edu.cn/2022/0429/c27469a694799/page.htm', 'https://xxxy.jnu.edu.cn/2022/0427/c27469a694063/page.htm', 'https://xxxy.jnu.edu.cn/2022/0426/c27469a693591/page.htm', 'https://xxxy.jnu.edu.cn/2022/0424/c27469a692645/page.htm', 'https://xxxy.jnu.edu.cn/2022/0418/c27469a690977/page.htm', 'https://xxxy.jnu.edu.cn/2022/0415/c27469a690759/page.htm', 'https://xxxy.jnu.edu.cn/2022/0415/c27469a690757/page.htm', 'https://xxxy.jnu.edu.cn/2022/0414/c27469a690349/page.htm', 'https://xxxy.jnu.edu.cn/2022/0408/c27469a689401/page.htm', 'https://xxxy.jnu.edu.cn/2022/0402/c27469a688625/page.htm', 'https://xxxy.jnu.edu.cn/2022/0107/c27469a676625/page.htm', 'https://xxxy.jnu.edu.cn/2022/0104/c27469a675555/page.htm', 'https://xxxy.jnu.edu.cn/2021/1217/c27469a671269/page.htm', 'https://xxxy.jnu.edu.cn/2021/1216/c27469a670837/page.htm', 'https://xxxy.jnu.edu.cn/2021/1208/c27469a667613/page.htm', 'https://xxxy.jnu.edu.cn/2021/1206/c27469a666973/page.htm', 'https://xxxy.jnu.edu.cn/2021/1126/c27469a664819/page.htm', 'https://xxxy.jnu.edu.cn/2021/1124/c27469a663925/page.htm', 'https://xxxy.jnu.edu.cn/2021/1116/c27469a661331/page.htm', 'https://xxxy.jnu.edu.cn/2021/1115/c27469a660877/page.htm', 'https://xxxy.jnu.edu.cn/2021/1115/c27469a660783/page.htm', 'https://xxxy.jnu.edu.cn/2021/1115/c27469a660739/page.htm', 'https://xxxy.jnu.edu.cn/2021/1108/c27469a659627/page.htm', 'https://xxxy.jnu.edu.cn/2021/1105/c27469a659295/page.htm', 'https://xxxy.jnu.edu.cn/2021/1103/c27469a658953/page.htm', 'https://xxxy.jnu.edu.cn/2021/1027/c27469a657413/page.htm', 'https://xxxy.jnu.edu.cn/2021/1027/c27469a657385/page.htm', 'https://xxxy.jnu.edu.cn/2021/1026/c27469a657169/page.htm', 'https://xxxy.jnu.edu.cn/2021/1026/c27469a657167/page.htm', 'https://xxxy.jnu.edu.cn/2021/1018/c27469a655455/page.htm', 'https://xxxy.jnu.edu.cn/2021/1011/c27469a654287/page.htm', 'https://xxxy.jnu.edu.cn/2021/1009/c27469a653609/page.htm', 'https://xxxy.jnu.edu.cn/2021/0930/c27469a652983/page.htm', 'https://xxxy.jnu.edu.cn/2021/0928/c27469a652409/page.htm', 'https://xxxy.jnu.edu.cn/2021/0918/c27469a649589/page.htm', 'https://xxxy.jnu.edu.cn/2021/0909/c27469a647843/page.htm', 'https://xxxy.jnu.edu.cn/2021/0908/c27469a647637/page.htm', 'https://xxxy.jnu.edu.cn/2021/0823/c27469a642171/page.htm', 'https://xxxy.jnu.edu.cn/2021/0814/c27469a641225/page.htm', 'https://xxxy.jnu.edu.cn/2021/0810/c27469a640811/page.htm', 'https://xxxy.jnu.edu.cn/2021/0707/c27469a636463/page.htm', 'https://xxxy.jnu.edu.cn/2021/0705/c27469a635715/page.htm', 'https://xxxy.jnu.edu.cn/2021/0624/c27469a633273/page.htm', 'https://xxxy.jnu.edu.cn/2021/0618/c27469a631717/page.htm', 'https://xxxy.jnu.edu.cn/2021/0602/c27469a629321/page.htm', 'https://xxxy.jnu.edu.cn/2021/0525/c27469a625749/page.htm', 'https://xxxy.jnu.edu.cn/2021/0524/c27469a625745/page.htm', 'https://xxxy.jnu.edu.cn/2021/0521/c27469a625743/page.htm', 'https://xxxy.jnu.edu.cn/2021/0519/c27469a625741/page.htm', 'https://xxxy.jnu.edu.cn/2021/0518/c27469a625739/page.htm', 'https://xxxy.jnu.edu.cn/2021/0511/c27469a621793/page.htm', 'https://xxxy.jnu.edu.cn/2021/0507/c27469a621787/page.htm', 'https://xxxy.jnu.edu.cn/2021/0506/c27469a621783/page.htm', 'https://xxxy.jnu.edu.cn/2021/0506/c27469a621779/page.htm', 'https://xxxy.jnu.edu.cn/2021/0421/c27469a621775/page.htm', 'https://xxxy.jnu.edu.cn/2021/0414/c27469a621773/page.htm', 'https://xxxy.jnu.edu.cn/2021/0407/c27469a621769/page.htm', 'https://xxxy.jnu.edu.cn/2021/0323/c27469a606433/page.htm', 'https://xxxy.jnu.edu.cn/2021/0319/c27469a606429/page.htm', 'https://xxxy.jnu.edu.cn/2021/0319/c27469a606427/page.htm', 'https://xxxy.jnu.edu.cn/2021/0309/c27469a606425/page.htm', 'https://xxxy.jnu.edu.cn/2021/0305/c27469a606423/page.htm', 'https://xxxy.jnu.edu.cn/2021/0204/c27469a606421/page.htm', 'https://xxxy.jnu.edu.cn/2021/0122/c27469a606419/page.htm', 'https://xxxy.jnu.edu.cn/2021/0108/c27469a606417/page.htm', 'https://xxxy.jnu.edu.cn/2020/1231/c27469a606413/page.htm', 'https://xxxy.jnu.edu.cn/2020/1224/c27469a606411/page.htm', 'https://xxxy.jnu.edu.cn/2020/1224/c27469a606409/page.htm', 'https://xxxy.jnu.edu.cn/2020/1224/c27469a606407/page.htm', 'https://xxxy.jnu.edu.cn/2020/1224/c27469a606405/page.htm', 'https://xxxy.jnu.edu.cn/2020/1221/c27469a573285/page.htm', 'https://xxxy.jnu.edu.cn/2020/1218/c27469a573281/page.htm', 'https://xxxy.jnu.edu.cn/2020/1214/c27469a573279/page.htm', 'https://xxxy.jnu.edu.cn/2020/1211/c27469a573273/page.htm', 'https://xxxy.jnu.edu.cn/2020/1207/c27469a573269/page.htm', 'https://xxxy.jnu.edu.cn/2020/1207/c27469a573265/page.htm', 'https://xxxy.jnu.edu.cn/2020/1126/c27469a573261/page.htm', 'https://xxxy.jnu.edu.cn/2020/1123/c27469a573251/page.htm', 'https://xxxy.jnu.edu.cn/2020/1116/c27469a573247/page.htm', 'https://xxxy.jnu.edu.cn/2020/1113/c27469a573243/page.htm', 'https://xxxy.jnu.edu.cn/2020/1103/c27469a573237/page.htm', 'https://xxxy.jnu.edu.cn/2020/0106/c27469a573207/page.htm', 'https://xxxy.jnu.edu.cn/2019/1231/c27469a573205/page.htm', 'https://xxxy.jnu.edu.cn/2019/1220/c27469a573203/page.htm', 'https://xxxy.jnu.edu.cn/2019/1220/c27469a573201/page.htm', 'https://xxxy.jnu.edu.cn/2019/1217/c27469a573195/page.htm', 'https://xxxy.jnu.edu.cn/2019/1216/c27469a573191/page.htm', 'https://xxxy.jnu.edu.cn/2019/1213/c27469a573189/page.htm', 'https://xxxy.jnu.edu.cn/2019/1212/c27469a573185/page.htm', 'https://xxxy.jnu.edu.cn/2019/1211/c27469a573183/page.htm', 'https://xxxy.jnu.edu.cn/2019/1209/c27469a573179/page.htm', 'https://xxxy.jnu.edu.cn/2019/1209/c27469a573175/page.htm', 'https://xxxy.jnu.edu.cn/2019/1206/c27469a573171/page.htm', 'https://xxxy.jnu.edu.cn/2019/1206/c27469a573169/page.htm', 'https://xxxy.jnu.edu.cn/2019/1203/c27469a573165/page.htm', 'https://xxxy.jnu.edu.cn/2019/1203/c27469a573161/page.htm', 'https://xxxy.jnu.edu.cn/2019/1203/c27469a573157/page.htm', 'https://xxxy.jnu.edu.cn/2019/1202/c27469a573155/page.htm', 'https://xxxy.jnu.edu.cn/2019/1202/c27469a573151/page.htm', 'https://xxxy.jnu.edu.cn/2019/1202/c27469a573147/page.htm', 'https://xxxy.jnu.edu.cn/2019/1127/c27469a573143/page.htm', 'https://xxxy.jnu.edu.cn/2019/1127/c27469a573141/page.htm', 'https://xxxy.jnu.edu.cn/2019/1121/c27469a573129/page.htm', 'https://xxxy.jnu.edu.cn/2019/1115/c27469a573119/page.htm', 'https://xxxy.jnu.edu.cn/2019/1114/c27469a573111/page.htm', 'https://xxxy.jnu.edu.cn/2019/1112/c27469a573109/page.htm', 'https://xxxy.jnu.edu.cn/2019/1108/c27469a573105/page.htm', 'https://xxxy.jnu.edu.cn/2019/1107/c27469a573099/page.htm', 'https://xxxy.jnu.edu.cn/2019/1107/c27469a573095/page.htm', 'https://xxxy.jnu.edu.cn/2019/1106/c27469a573093/page.htm', 'https://xxxy.jnu.edu.cn/2019/1106/c27469a573089/page.htm', 'https://xxxy.jnu.edu.cn/2019/1105/c27469a573087/page.htm', 'https://xxxy.jnu.edu.cn/2019/1104/c27469a573079/page.htm', 'https://xxxy.jnu.edu.cn/2019/1031/c27469a573075/page.htm', 'https://xxxy.jnu.edu.cn/2019/1028/c27469a573069/page.htm', 'https://xxxy.jnu.edu.cn/2019/1028/c27469a573067/page.htm', 'https://xxxy.jnu.edu.cn/2019/1025/c27469a573063/page.htm', 'https://xxxy.jnu.edu.cn/2019/1017/c27469a573055/page.htm', 'https://xxxy.jnu.edu.cn/2019/1010/c27469a573053/page.htm', 'https://xxxy.jnu.edu.cn/2019/1010/c27469a573049/page.htm', 'https://xxxy.jnu.edu.cn/2019/1008/c27469a573047/page.htm', 'https://xxxy.jnu.edu.cn/2019/0919/c27469a573041/page.htm', 'https://xxxy.jnu.edu.cn/2019/0919/c27469a573039/page.htm', 'https://xxxy.jnu.edu.cn/2019/0918/c27469a573033/page.htm', 'https://xxxy.jnu.edu.cn/2019/0917/c27469a573031/page.htm', 'https://xxxy.jnu.edu.cn/2019/0917/c27469a573029/page.htm', 'https://xxxy.jnu.edu.cn/2019/0916/c27469a573027/page.htm', 'https://xxxy.jnu.edu.cn/2019/0916/c27469a573025/page.htm', 'https://xxxy.jnu.edu.cn/2019/0904/c27469a573021/page.htm', 'https://xxxy.jnu.edu.cn/2019/0904/c27469a573019/page.htm', 'https://xxxy.jnu.edu.cn/2019/0904/c27469a573017/page.htm', 'https://xxxy.jnu.edu.cn/2019/0903/c27469a573013/page.htm', 'https://xxxy.jnu.edu.cn/2019/0717/c27469a573011/page.htm', 'https://xxxy.jnu.edu.cn/2019/0711/c27469a573009/page.htm', 'https://xxxy.jnu.edu.cn/2019/0711/c27469a573007/page.htm', 'https://xxxy.jnu.edu.cn/2019/0710/c27469a573005/page.htm', 'https://xxxy.jnu.edu.cn/2019/0703/c27469a572991/page.htm', 'https://xxxy.jnu.edu.cn/2019/0703/c27469a572989/page.htm', 'https://xxxy.jnu.edu.cn/2019/0703/c27469a572985/page.htm', 'https://xxxy.jnu.edu.cn/2019/0626/c27469a572983/page.htm', 'https://xxxy.jnu.edu.cn/2019/0626/c27469a572981/page.htm', 'https://xxxy.jnu.edu.cn/2019/0624/c27469a572979/page.htm', 'https://xxxy.jnu.edu.cn/2019/0619/c27469a572975/page.htm', 'https://xxxy.jnu.edu.cn/2019/0618/c27469a572973/page.htm', 'https://xxxy.jnu.edu.cn/2019/0605/c27469a572959/page.htm', 'https://xxxy.jnu.edu.cn/2019/0531/c27469a572951/page.htm', 'https://xxxy.jnu.edu.cn/2019/0524/c27469a572943/page.htm', 'https://xxxy.jnu.edu.cn/2019/0522/c27469a572939/page.htm', 'https://xxxy.jnu.edu.cn/2019/0516/c27469a572935/page.htm', 'https://xxxy.jnu.edu.cn/2019/0515/c27469a572931/page.htm', 'https://xxxy.jnu.edu.cn/2019/0514/c27469a572929/page.htm', 'https://xxxy.jnu.edu.cn/2019/0514/c27469a572927/page.htm', 'https://xxxy.jnu.edu.cn/2019/0514/c27469a572923/page.htm', 'https://xxxy.jnu.edu.cn/2019/0508/c27469a572921/page.htm', 'https://xxxy.jnu.edu.cn/2019/0506/c27469a572919/page.htm', 'https://xxxy.jnu.edu.cn/2019/0505/c27469a572917/page.htm', 'https://xxxy.jnu.edu.cn/2019/0505/c27469a572913/page.htm', 'https://xxxy.jnu.edu.cn/2019/0426/c27469a572905/page.htm', 'https://xxxy.jnu.edu.cn/2019/0423/c27469a572903/page.htm', 'https://xxxy.jnu.edu.cn/2019/0422/c27469a572897/page.htm', 'https://xxxy.jnu.edu.cn/2019/0418/c27469a572893/page.htm', 'https://xxxy.jnu.edu.cn/2019/0320/c27469a572891/page.htm', 'https://xxxy.jnu.edu.cn/2019/0318/c27469a572887/page.htm', 'https://xxxy.jnu.edu.cn/2019/0318/c27469a572883/page.htm', 'https://xxxy.jnu.edu.cn/2019/0315/c27469a572879/page.htm', 'https://xxxy.jnu.edu.cn/2019/0304/c27469a572867/page.htm', 'https://xxxy.jnu.edu.cn/2019/0301/c27469a572863/page.htm', 'https://xxxy.jnu.edu.cn/2018/1226/c27469a572855/page.htm', 'https://xxxy.jnu.edu.cn/2018/1224/c27469a572851/page.htm', 'https://xxxy.jnu.edu.cn/2018/1224/c27469a572845/page.htm', 'https://xxxy.jnu.edu.cn/2018/1221/c27469a572841/page.htm', 'https://xxxy.jnu.edu.cn/2018/1221/c27469a572839/page.htm', 'https://xxxy.jnu.edu.cn/2018/1220/c27469a572837/page.htm', 'https://xxxy.jnu.edu.cn/2018/1217/c27469a572829/page.htm', 'https://xxxy.jnu.edu.cn/2018/1210/c27469a572821/page.htm', 'https://xxxy.jnu.edu.cn/2018/1203/c27469a572819/page.htm', 'https://xxxy.jnu.edu.cn/2018/1129/c27469a572815/page.htm', 'https://xxxy.jnu.edu.cn/2018/1127/c27469a572813/page.htm', 'https://xxxy.jnu.edu.cn/2018/1126/c27469a572803/page.htm', 'https://xxxy.jnu.edu.cn/2018/1126/c27469a572801/page.htm', 'https://xxxy.jnu.edu.cn/2018/1123/c27469a572797/page.htm', 'https://xxxy.jnu.edu.cn/2018/1122/c27469a572793/page.htm', 'https://xxxy.jnu.edu.cn/2018/1121/c27469a572787/page.htm', 'https://xxxy.jnu.edu.cn/2018/1121/c27469a572785/page.htm', 'https://xxxy.jnu.edu.cn/2018/1119/c27469a572781/page.htm', 'https://xxxy.jnu.edu.cn/2018/1119/c27469a572779/page.htm', 'https://xxxy.jnu.edu.cn/2018/1116/c27469a572773/page.htm', 'https://xxxy.jnu.edu.cn/2018/1115/c27469a572771/page.htm', 'https://xxxy.jnu.edu.cn/2018/1115/c27469a572769/page.htm', 'https://xxxy.jnu.edu.cn/2018/1114/c27469a572767/page.htm', 'https://xxxy.jnu.edu.cn/2018/1113/c27469a572763/page.htm', 'https://xxxy.jnu.edu.cn/2018/1107/c27469a572755/page.htm', 'https://xxxy.jnu.edu.cn/2018/1102/c27469a572751/page.htm', 'https://xxxy.jnu.edu.cn/2018/1019/c27469a572749/page.htm', 'https://xxxy.jnu.edu.cn/2018/1018/c27469a572737/page.htm', 'https://xxxy.jnu.edu.cn/2018/1017/c27469a572735/page.htm', 'https://xxxy.jnu.edu.cn/2018/1017/c27469a572731/page.htm', 'https://xxxy.jnu.edu.cn/2018/1017/c27469a572725/page.htm', 'https://xxxy.jnu.edu.cn/2018/1017/c27469a572723/page.htm', 'https://xxxy.jnu.edu.cn/2018/1017/c27469a572719/page.htm', 'https://xxxy.jnu.edu.cn/2018/1015/c27469a572707/page.htm', 'https://xxxy.jnu.edu.cn/2018/1010/c27469a572705/page.htm', 'https://xxxy.jnu.edu.cn/2018/1010/c27469a572701/page.htm', 'https://xxxy.jnu.edu.cn/2018/1008/c27469a572699/page.htm', 'https://xxxy.jnu.edu.cn/2018/0907/c27469a572695/page.htm', 'https://xxxy.jnu.edu.cn/2018/0905/c27469a572691/page.htm', 'https://xxxy.jnu.edu.cn/2018/0713/c27469a572685/page.htm', 'https://xxxy.jnu.edu.cn/2018/0710/c27469a572671/page.htm', 'https://xxxy.jnu.edu.cn/2018/0606/c27469a572661/page.htm', 'https://xxxy.jnu.edu.cn/2018/0524/c27469a572659/page.htm', 'https://xxxy.jnu.edu.cn/2018/0524/c27469a572655/page.htm', 'https://xxxy.jnu.edu.cn/2018/0524/c27469a572653/page.htm', 'https://xxxy.jnu.edu.cn/2018/0522/c27469a572649/page.htm', 'https://xxxy.jnu.edu.cn/2018/0522/c27469a572645/page.htm', 'https://xxxy.jnu.edu.cn/2018/0509/c27469a572635/page.htm', 'https://xxxy.jnu.edu.cn/2018/0507/c27469a572631/page.htm', 'https://xxxy.jnu.edu.cn/2018/0419/c27469a572625/page.htm', 'https://xxxy.jnu.edu.cn/2018/0416/c27469a572621/page.htm', 'https://xxxy.jnu.edu.cn/2018/0413/c27469a572619/page.htm', 'https://xxxy.jnu.edu.cn/2018/0327/c27469a572609/page.htm', 'https://xxxy.jnu.edu.cn/2018/0320/c27469a572605/page.htm', 'https://xxxy.jnu.edu.cn/2018/0314/c27469a572603/page.htm', 'https://xxxy.jnu.edu.cn/2018/0117/c27469a572597/page.htm', 'https://xxxy.jnu.edu.cn/2018/0105/c27469a572591/page.htm', 'https://xxxy.jnu.edu.cn/2018/0103/c27469a572587/page.htm', 'https://xxxy.jnu.edu.cn/2018/0103/c27469a572585/page.htm', 'https://xxxy.jnu.edu.cn/2018/0103/c27469a572583/page.htm', 'https://xxxy.jnu.edu.cn/2018/0103/c27469a572579/page.htm', 'https://xxxy.jnu.edu.cn/2017/1229/c27469a572575/page.htm', 'https://xxxy.jnu.edu.cn/2017/1221/c27469a572563/page.htm', 'https://xxxy.jnu.edu.cn/2017/1213/c27469a572555/page.htm', 'https://xxxy.jnu.edu.cn/2017/1213/c27469a572551/page.htm', 'https://xxxy.jnu.edu.cn/2017/1211/c27469a572547/page.htm', 'https://xxxy.jnu.edu.cn/2017/1129/c27469a572543/page.htm', 'https://xxxy.jnu.edu.cn/2017/1122/c27469a572535/page.htm', 'https://xxxy.jnu.edu.cn/2017/1121/c27469a572531/page.htm', 'https://xxxy.jnu.edu.cn/2017/1121/c27469a572529/page.htm', 'https://xxxy.jnu.edu.cn/2017/1115/c27469a572523/page.htm', 'https://xxxy.jnu.edu.cn/2017/1115/c27469a572519/page.htm', 'https://xxxy.jnu.edu.cn/2017/1113/c27469a572517/page.htm', 'https://xxxy.jnu.edu.cn/2017/1107/c27469a572511/page.htm', 'https://xxxy.jnu.edu.cn/2017/1023/c27469a572503/page.htm', 'https://xxxy.jnu.edu.cn/2017/1023/c27469a572499/page.htm', 'https://xxxy.jnu.edu.cn/2017/1017/c27469a572495/page.htm', 'https://xxxy.jnu.edu.cn/2017/1013/c27469a572487/page.htm', 'https://xxxy.jnu.edu.cn/2017/1013/c27469a572485/page.htm', 'https://xxxy.jnu.edu.cn/2017/0926/c27469a572477/page.htm', 'https://xxxy.jnu.edu.cn/2017/0919/c27469a572469/page.htm', 'https://xxxy.jnu.edu.cn/2017/0919/c27469a572465/page.htm', 'https://xxxy.jnu.edu.cn/2017/0912/c27469a572457/page.htm', 'https://xxxy.jnu.edu.cn/2017/0902/c27469a572455/page.htm', 'https://xxxy.jnu.edu.cn/2017/0826/c27469a572451/page.htm', 'https://xxxy.jnu.edu.cn/2017/0728/c27469a572449/page.htm', 'https://xxxy.jnu.edu.cn/2017/0717/c27469a572445/page.htm', 'https://xxxy.jnu.edu.cn/2017/0705/c27469a572435/page.htm', 'https://xxxy.jnu.edu.cn/2017/0628/c27469a572431/page.htm', 'https://xxxy.jnu.edu.cn/2017/0621/c27469a572429/page.htm', 'https://xxxy.jnu.edu.cn/2017/0619/c27469a572425/page.htm', 'https://xxxy.jnu.edu.cn/2017/0609/c27469a572409/page.htm', 'https://xxxy.jnu.edu.cn/2017/0605/c27469a572403/page.htm', 'https://xxxy.jnu.edu.cn/2017/0605/c27469a572401/page.htm', 'https://xxxy.jnu.edu.cn/2017/0602/c27469a572395/page.htm', 'https://xxxy.jnu.edu.cn/2017/0602/c27469a572391/page.htm', 'https://xxxy.jnu.edu.cn/2017/0601/c27469a572389/page.htm', 'https://xxxy.jnu.edu.cn/2017/0531/c27469a572385/page.htm', 'https://xxxy.jnu.edu.cn/2017/0531/c27469a572383/page.htm', 'https://xxxy.jnu.edu.cn/2017/0522/c27469a572381/page.htm', 'https://xxxy.jnu.edu.cn/2017/0519/c27469a572375/page.htm', 'https://xxxy.jnu.edu.cn/2017/0509/c27469a572363/page.htm', 'https://xxxy.jnu.edu.cn/2017/0330/c27469a572335/page.htm', 'https://xxxy.jnu.edu.cn/2017/0321/c27469a572329/page.htm', 'https://xxxy.jnu.edu.cn/2017/0227/c27469a572317/page.htm', 'https://xxxy.jnu.edu.cn/2017/0112/c27469a572315/page.htm', 'https://xxxy.jnu.edu.cn/2017/0109/c27469a572311/page.htm', 'https://xxxy.jnu.edu.cn/2017/0103/c27469a572303/page.htm', 'https://xxxy.jnu.edu.cn/2016/1226/c27469a572297/page.htm', 'https://xxxy.jnu.edu.cn/2016/1219/c27469a572291/page.htm', 'https://xxxy.jnu.edu.cn/2016/1215/c27469a572287/page.htm', 'https://xxxy.jnu.edu.cn/2016/1212/c27469a572279/page.htm', 'https://xxxy.jnu.edu.cn/2016/1205/c27469a572277/page.htm', 'https://xxxy.jnu.edu.cn/2016/1129/c27469a572275/page.htm', 'https://xxxy.jnu.edu.cn/2016/1123/c27469a572271/page.htm', 'https://xxxy.jnu.edu.cn/2016/1122/c27469a572267/page.htm', 'https://xxxy.jnu.edu.cn/2016/1116/c27469a572261/page.htm', 'https://xxxy.jnu.edu.cn/2016/1115/c27469a572259/page.htm', 'https://xxxy.jnu.edu.cn/2016/1114/c27469a572253/page.htm', 'https://xxxy.jnu.edu.cn/2016/1111/c27469a572251/page.htm', 'https://xxxy.jnu.edu.cn/2016/1110/c27469a572247/page.htm', 'https://xxxy.jnu.edu.cn/2016/1109/c27469a572243/page.htm', 'https://xxxy.jnu.edu.cn/2016/1109/c27469a572235/page.htm', 'https://xxxy.jnu.edu.cn/2016/1107/c27469a572233/page.htm', 'https://xxxy.jnu.edu.cn/2016/1102/c27469a572229/page.htm', 'https://xxxy.jnu.edu.cn/2016/1102/c27469a572227/page.htm', 'https://xxxy.jnu.edu.cn/2016/1028/c27469a572205/page.htm', 'https://xxxy.jnu.edu.cn/2016/1017/c27469a572183/page.htm', 'https://xxxy.jnu.edu.cn/2016/1010/c27469a572163/page.htm', 'https://xxxy.jnu.edu.cn/2016/0930/c27469a572143/page.htm', 'https://xxxy.jnu.edu.cn/2016/0927/c27469a572141/page.htm', 'https://xxxy.jnu.edu.cn/2016/0923/c27469a572133/page.htm', 'https://xxxy.jnu.edu.cn/2016/0921/c27469a572129/page.htm', 'https://xxxy.jnu.edu.cn/2016/0919/c27469a572123/page.htm', 'https://xxxy.jnu.edu.cn/2016/0905/c27469a572111/page.htm', 'https://xxxy.jnu.edu.cn/2016/0714/c27469a572107/page.htm', 'https://xxxy.jnu.edu.cn/2016/0712/c27469a572101/page.htm', 'https://xxxy.jnu.edu.cn/2016/0629/c27469a572097/page.htm', 'https://xxxy.jnu.edu.cn/2016/0628/c27469a572093/page.htm', 'https://xxxy.jnu.edu.cn/2016/0615/c27469a572081/page.htm', 'https://xxxy.jnu.edu.cn/2016/0615/c27469a572077/page.htm', 'https://xxxy.jnu.edu.cn/2016/0613/c27469a572071/page.htm', 'https://xxxy.jnu.edu.cn/2016/0607/c27469a572067/page.htm', 'https://xxxy.jnu.edu.cn/2016/0526/c27469a572065/page.htm', 'https://xxxy.jnu.edu.cn/2016/0427/c27469a572051/page.htm', 'https://xxxy.jnu.edu.cn/2016/0418/c27469a572035/page.htm', 'https://xxxy.jnu.edu.cn/2016/0418/c27469a572033/page.htm', 'https://xxxy.jnu.edu.cn/2016/0401/c27469a572011/page.htm', 'https://xxxy.jnu.edu.cn/2016/0401/c27469a572007/page.htm', 'https://xxxy.jnu.edu.cn/2016/0330/c27469a571997/page.htm', 'https://xxxy.jnu.edu.cn/2016/0330/c27469a571993/page.htm']

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}


pass_webs = []
with open('pass_webs_JD.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]  # 假设网址在第一列
        if url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url  # 添加模式
            pass_webs.append(url)

print(pass_webs)


log_path = 'format_JD.csv'
file = open(log_path, 'a+', encoding='utf-8', newline='')
with open(log_path, "w", newline="") as format:
        format.truncate()
csv_writer = csv.writer(file)

csv_writer.writerow([f'讲座标题', '报告人', '时间', '地点', '大学', "通知全文链接","通知发布时间", "通知内容", "报告人简介"])

for web in webs:

    print("web:", web)
    if web in pass_webs:
        continue
    
    # 发送 HTTP 请求获取页面内容
    response = requests.get(web, headers = headers, verify= False)
    response.encoding = 'utf-8'
    html_content = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")
 

    publish_timess = soup.find("p", class_ = "article-small")
    publish_times = publish_timess.text.strip()
    pbs = re.split(r"发布时间：|来源：", publish_times)
    pbs = [i.strip() for i in pbs if i.strip()]
    publish_time = pbs[0]

    contentss = soup.find("div", class_ = "article-content")
    contents = contentss.text.strip()
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

        
    print("标题:", title)
    print("通知发布时间:", publish_time)
    print("演讲者:", speaker)
    print("时间:", time)
    print("地点:", location)
    print("演讲者简介:", speaker_file)
    print("演讲内容:", content)
    print("-------------------")

    csv_writer.writerow([title, speaker, time, location, "暨南大学", web, publish_time, content, speaker_file])

file.close()