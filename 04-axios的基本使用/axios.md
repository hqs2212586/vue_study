## 一、介绍

Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。 [官方资料和介绍](https://www.kancloud.cn/yunye/axios/234845)

- 从浏览器中创建 [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- 从 node.js 创建 [http](http://nodejs.org/api/http.html) 请求
- 支持 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) API
- 拦截请求和响应
- 转换请求数据和响应数据
- 取消请求
- 自动转换 JSON 数据
- 客户端支持防御 [XSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery)

## 二、Axios的基本使用

### 1、Axios安装方法

使用npm：
```
$ npm install axios
```

使用bower：
```
$ bower install axios
```

使用cdn：
```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

### 2、axios项目配置准备
```
$ npm init --yes
{
  "name": "code",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}

$ npm install vue -S;npm install axios -S
code@1.0.0 /Users/hqs/PycharmProjects/vue_study/04-axios的基本使用/code
└── vue@2.6.10 

code@1.0.0 /Users/hqs/PycharmProjects/vue_study/04-axios的基本使用/code
└─┬ axios@0.18.0 
  ├─┬ follow-redirects@1.7.0 
  │ └─┬ debug@3.2.6 
  │   └── ms@2.1.1 
  └── is-buffer@1.1.6 
```

### 3、服务端配置准备
```python
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
```
服务端代码如上所示，再编辑user.json文件如下：
```
[{"name": "alex"}]
```

### 4、axios发送请求
axios源码：

#### (1) 发起一个GET请求
```javascript
methods:{
    sendAjax(){
        // 发送get请求
        axios.get("http://127.0.0.1:8800/"
        ).then(res=>{
            console.log(res.data);        // <h2>首页</h2>
            console.log(typeof res.data);    // string
            this.msg = res.data;
        }).catch(err=>{   // 有参数括号可以不写
            console.log(err);
        })
    }
}
```
点击发送get请求的按钮，console输出的实例化对象如下所示：

![get请求](https://www.cnblogs.com/images/cnblogs_com/xiugeng/1453382/o_1556293318984.jpg)

#### (2)发起一个POST请求

```javascript
methods:{
    sendAjaxByPost(){
        var params = new URLSearchParams();
        params.append('name', 'hqs');
        // 发送post请求
        axios.post('http://127.0.0.1:8800/create', params
        ).then(function (res) {
            console.log(res);
        }).catch(err=>{
            console.log(err);
        })
    }
}
```
点击发送post请求，console输出的实例化对象如下所示：
![post请求](https://www.cnblogs.com/images/cnblogs_com/xiugeng/1453382/o_1556334515951.jpg)

user.json文件内容变化为如下内容：
```[{"name": "alex"}, {"name": "hqs"}]```

### 5、axios的默认配置




