import requests
from lxml import etree
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os
import re
import pandas as pd

df = pd.read_csv("data2.csv")
li = list(df['通知发布时间'])
for ti in li:
    print(ti)