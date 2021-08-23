from flask import Flask, render_template
import sqlite3
from crawler import datapro, spider


app = Flask(__name__)



@app.route('/')
def index():
    dbpath = "info.db"
    numlist = datapro.stats(dbpath)
    return render_template("index.html", nums=numlist)


@app.route('/index')
def index2():
    return index()


@app.route('/index.html')
def home():
    return index()


@app.route('/allInfo')
def allInfo():
    dbpath = "info.db"
    datalist = datapro.allinfos(dbpath)
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
