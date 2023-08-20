import pandas as pd
import re

df = pd.read_csv("3.csv")


for index, row in df.iterrows():
    print(row)
    ti = df.loc[index, "时间"]
    new_ti = re.split(" ", ti)
    df.loc[index, "时间"] = new_ti[0]

    ti = df.loc[index, "通知发布时间"]
    new_ti = re.split(" ", ti)
    df.loc[index, "通知发布时间"] = new_ti[0]
    print(row)

df.to_csv('4.csv', index = False)