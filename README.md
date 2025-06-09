# 关于 python-talk
Using Python + Flask  + Vue + Axios + JWT to build a forum.

# 如何在本地运行后端(backend) 

- clone

```shell
$ git clone https://github.com/codists/python-talk.git
```

- create and activate virtual environment

```shell
$ cd python-talk/backend/
backend$ source ./venv/bin/activate
```

- install requirements.txt

```shell
python-talk/backend$ pip install -r requirements.txt
```

- run 

```shell
python-talk/backend$ flask run
```
# 如何在本地运行前端(frontend)
- clone
    ```shell
    $ git clone https://github.com/codists/python-talk.git
    ```
- install 
    ```shell
    $ cd python-talk/frontend/
     python-talk/frontend$ npm install
    ```
- run
    ```shell
    python-talk/frontend$ npm run serve
    ```

# 如何部署

采用 Docker、Nginx、Ubuntu 进行部署。

## 部署目录结构

虽然 python_talk 只是一个应用(application)，但考虑到部署在不同服务器之间迁移的灵活性，以及和其它应用之间的协调性，采用下面的部署结构，当然，这样的结构稍显复杂：

```├── backend
/www# tree -L 4 "$(pwd)"
/www
├── backend
│   └── python_talk
│       └── backend
│           ├── Dockerfile
│           ├── README.md
│           ├── README_zh.md
│           ├── docker-compose-common.yml
│           ├── docker-compose.yml
│           ├── docs
│           ├── migrations
│           ├── python_talk
│           ├── requirements.txt
│           └── setup.py
├── common
│   ├── docker-compose.yml
│   ├── nginx
│   │   ├── conf.d
│   │   │   └── python_talk.conf
│   │   ├── logs
│   │   │   ├── access.log
│   │   │   ├── error.log
│   │   │   └── python_talk
│   │   └── nginx.conf

│   └── redis
│       ├── conf
│       │   ├── redis.conf
│       │   ├── with-cache.data
│       │   └── without-cache.data
│       └── data
│           └── dump.rdb
└── frontend
    └── python_talk
        └── dist
            ├── css
            ├── favicon.ico
            ├── img
            ├── index.html
            ├── js
            └── report.html
```

## 部署流程

一般来说，部署时是不需要拉取代码仓库的，前端直接上传 dist 目录，后端直接上传代码即可。这里这样做是为了让不熟悉该流程的人更好的理解。

```
# 目录设置
mkdir -p /www/backend/python_talk
mkdir -p /www/frontend/python_talk
mkdir -p /www/common/{mysql,nginx,redis} 

# 拉取代码
cd /www/temp
git clone https://github.com/codists/python-talk.git

# 前端打包，这一步可以
cd /www/temp/python-talk/frontend





```

