# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 1.pip3 install Flask
# 2.python3 server.py

import json

from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)

# 默认是get请求
@app.route("/")
def index():
    resp = Response("<h2>首页</h2>")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/course")
def courses():
    resp = Response(json.dumps({
        "name": "alex"
    }))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/create", methods=["post",])
def create():
    print(request.form.get('name'))

    with open("user.json", "r") as f:
        # 将数据反序列化
        data = json.loads(f.read())

    data.append({"name": request.form.get('name')})

    with open("user.json", "w") as f:
        f.write(json.dumps(data))

    resp = Response(json.dumps(data))
    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

if __name__ == '__main__':
    app.run(host="localhost", port=8800)


