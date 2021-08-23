# -*- codeing = utf-8 -*-
# @Time : 2021/8/19 1:06
# @Author : TobiasKruzhor
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import sqlite3


def main():
    baseurl = "http://kjt.shandong.gov.cn/col/col13360/index.html"
    # 1、 爬取网页
    datalist = getData(baseurl)
    dbpath = "../info.db"
    # 3、 保存数据
    saveDateDB(datalist, dbpath)

    # askURL("http://kjt.shandong.gov.cn/col/col13360/index.html")


# 信息标题规则
findName = re.compile(r'<s></s>(.*?)</a>')
# 信息详情链接
findLink = re.compile(r'<a target="_blank" href="(.*?)" class="ellipsis-line-clamp">')
# 信息发布时间
findDate = re.compile(r'<span class="pull-right">(.*?)</span>')


# 爬取网页
def getData(baseurl):
    datalist = []
    url = str(baseurl)
    html = askURL(url)  # 保存获取到的网页源码
    # 2、 逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in re.findall(r"<li>(.*?)</li>",html):  # 查找符合要求的字符串，形成列表
        # print(item)   # 测试查看通知信息item全部信息
        data = []  # 保存一则通知的所有信息
        item = str(item)
        # 添加信息标题
        name = re.findall(findName, item)[0]
        data.append(name)
        # 添加信息链接
        link = re.findall(findLink, item)[0]
        data.append(link)
        # 添加信息发布时间
        date = re.findall(findDate, item)[0]
        data.append(date)
        # 信息放入datalist
        datalist.append(data)
    # nprint(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }  # 用户代理，告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的消息）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

# 保存数据
#
def saveDateDB(datalist, dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into info(
            info_name, info_link, info_date
            )
            values(%s)
        '''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("save")


if __name__ == "__main__":      # 当程序执行时
    # 调用函数
    main()
    # init_db("testdb.db")

    print("爬取完成")
