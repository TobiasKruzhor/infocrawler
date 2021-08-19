from flask import Flask, render_template
import sqlite3
import crawler


app = Flask(__name__)


@app.route('/')
def index():
    numlist = []
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    sql1 = "SELECT COUNT(*) FROM info"
    num1 = cur.execute(sql1)
    numlist.append(num1)

    sql2 = "SELECT COUNT(id) FROM info WHERE info_ava > 0"
    num2 = cur.execute(sql2)
    numlist.append(num2)

    sql3 = "SELECT COUNT(id) FROM info WHERE info_progress = 1"
    num3 = cur.execute(sql3)
    numlist.append(num3)

    sql4 = "SELECT COUNT(id) FROM info WHERE info_progress = 2"
    num4 = cur.execute(sql4)
    numlist.append(num4)
    cur.close()
    con.close()
    return render_template("index.html", nums=numlist)


@app.route('/index')
def index2():
    return index()


@app.route('/index.html')
def home():
    return index()


@app.route('/allInfo')
def allInfo():
    datalist = []
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    sql = "select * from info order by info_date desc"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("allInfo.html", infos=datalist)


@app.route('/process')
def process():
    return render_template("process.html")


@app.route('/doing')
def doing():
    return render_template("doing.html")


@app.route('/complete')
def complete():
    return render_template("complete.html")


if __name__ == '__main__':
    app.run()
