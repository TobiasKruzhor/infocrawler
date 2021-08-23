# -*- codeing = utf-8 -*-
# @Time : 2021/8/19 10:55
# @Author : TobiasKruzhor
# @File : datapro.py
# @Software : PyCharm
import sqlite3

def main():
    dbpath = "../info.db"
    stats(dbpath)
    allinfos(dbpath)
    #allInfo()


# 统计，统计数据库中数据量。
def stats(dbpath):
    numlist = []
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    # 全部信息
    sql = "SELECT COUNT(*) FROM info"
    data = cur.execute(sql)
    for item in data:
        numlist.append(item[0])

    # 已处理信息
    sql = "SELECT COUNT(*) FROM info WHERE info_ava>0"
    data = cur.execute(sql)
    for item in data:
        numlist.append(item[0])

    # 正在进行信息
    sql = "SELECT COUNT(*) FROM info WHERE info_progress=1"
    data = cur.execute(sql)
    for item in data:
        numlist.append(item[0])

    # 已完成信息
    sql = "SELECT COUNT(*) FROM info WHERE info_progress=2"
    data = cur.execute(sql)
    for item in data:
        numlist.append(item[0])
    cur.close()
    con.close()
    # print(numlist)
    return numlist


def allinfos(dbpath):
    datalist = []
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    sql = "select * from info order by info_date desc"
    data = cur.execute(sql)
    for item in data:
        # print(item)
        # print(item[4])
        if item[4] == 0:
            item4 = "未处理"
        elif item[4] == 1:
            item4 = "符合条件"
        elif item[4] == 2:
            item4 = "不符合条件"
        if item[5] == 0:
            item5 = "未进行"
        elif item[5] == 1:
            item5 = "进行中"
        elif item[5] == 2:
            item5 = "暂停"
        elif item[5] == 3:
            item5 = "完成"
        items = item[0:4] + (item4, item5)
        datalist.append(items)
    cur.close()
    con.close()
    # print(datalist)
    return datalist

if __name__ == "__main__":      # 当程序执行时
    # 调用函数
    main()