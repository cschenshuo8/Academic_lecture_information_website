import os
import sys
import webbrowser
import psutil

BASE_PATH = os.path.abspath('.')
# 重复点击开始即关闭原来服务重新打开
os.system('TASKKILL /F /IM manage.exe')


def run_main():
    sys.path.append("libs")
    url = 'http://127.0.0.1:8080'
    webbrowser.open_new(url)
    main = BASE_PATH + "/manage.exe runserver 8080 --noreload"
    print('--------------------------')
    print('系统已运行，可关闭此终端.')
    print('--------------------------')
    os.system(main)


run_main()

