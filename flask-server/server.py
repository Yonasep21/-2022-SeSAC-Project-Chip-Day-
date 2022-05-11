from flask import Flask, redirect, url_for

import db.db
from db.db import conn, cursor
from db.from_db import db_select
import pymysql

app = Flask(__name__)

#redirect -> all
@app.route('/')
def index():
    return redirect("http://127.0.0.1:5000/all")

# member api route
@app.route("/test")
def members():
    return {"tests": ["Test1", "Test2", "Test3"]}


@app.route("/all")
def ott():
    cursor = db.db.cursor()
    sql = f'SELECT * FROM MovieInfo;'
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    return {"Data": res}


@app.route("/contents/id/<id>")
def get_info_id(id):
    cursor = db.db.cursor()
    sql = f'SELECT * FROM MovieInfo WHERE KinoId = {id};'
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    return {"Data": res}

@app.route("/contents/title/<title>")
def get_info_title(title):
    cursor = db.db.cursor()
    sql = "SELECT * FROM MovieInfo WHERE TitleKr LIKE '%"+title+"%';"
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    return {"Data": res}

@app.route("/review/<id>")
def get_review(id):
    cursor = db.db.cursor()
    sql = f'SELECT * FROM MovieReview WHERE KinoId = {id};'
    cursor.execute(sql)
    res = cursor.fetchall()
    return {"Data": res}

@app.route("/img/<id>")
def get_img(id):
    cursor = db.db.cursor()
    sql = f'SELECT * FROM ImgUrl WHERE KinoId = {id};'
    cursor.execute(sql)
    res = cursor.fetchall()
    return {"Data": res}

@app.route("/ott/<ott>")
def getott(ott):
    if ott == 'netflix':
        ott = "넷플릭스"
    cursor = db.db.cursor()
    sql = "SELECT * FROM MovieInfo WHERE OttLinks like '%"+ ott +"%';"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(type(res))
    return {"Data": res}

if __name__ == "__main__":
    app.run(debug=True)
