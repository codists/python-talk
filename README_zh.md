# 关于 python-talk
Using Python + Flask  + Vue + Axios + JWT to build a forum.

# 如何在本地运行后端(backend) 

- clone

```shell
git clone https://github.com/codists/python-talk.git
```

- create and activate virtual environment

```shell
cd python-talk/backend/
source ./venv/bin/activate
```

- install requirements.txt

```shell
pip install -r requirements.txt
```

- run 

```shell
flask run
```
# 如何在本地运行前端(frontend)
- clone
    ```shell
    git clone https://github.com/codists/python-talk.git
    ```
- install 
    ```shell
    cd python-talk/frontend/
    npm install
    ```
- run
    ```shell
    npm run serve
    ```

# 如何在生产环境部署

采用 Docker、Nginx、Ubuntu 进行部署。

## 部署目录结构

虽然 python_talk 只是一个应用(application)，但考虑到部署在不同服务器之间迁移的灵活性，以及和其它应用之间的协调性，采用下面的部署结构，当然，这样的结构稍显复杂：

```├── backend
/www$ tree -L 4 "$(pwd)"
/www
├── backend
│   └── python_talk
│       └── backend
│           ├── Dockerfile
│           ├── README.md
│           ├── docker-compose.yml
│           ├── migrations
│           ├── python_talk
│           ├── requirements.txt
│           └── setup.py
├── common
│   ├── docker-compose-common.yml
│   ├── mysql
│   │   ├── conf.d
│   │   │   └── custome.conf
│   │   └── data
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
│       │   └── redis.conf
│       └── data
│           └── dump.rdb
└── frontend
    └── python_talk
        └── dist
            ├── css
            ├── favicon.ico
            ├── img
            ├── index.html
            └── js
```

## 部署流程

一般来说，部署时是不需要拉取代码仓库的，前端直接上传 dist 目录，后端直接上传代码即可。这里这样做是为了让不熟悉该流程的人更好的理解。

```
# 拉取代码
mkdir -p /www/code
cd /www/code
git clone https://github.com/codists/python-talk.git

# 前端(frontend)设置
mkdir -p /www/frontend/python_talk
cd /www/code/python-talk/frontend
npm install # 如果未安装 npm, 先安装 npm, 示例：sudo apt install npm -y
npm run build # 得到一个 dist 目录
cp -r /www/code/python-talk/frontend/dist /www/frontend/python_talk/

# 公共应用(mysql, redis, nginx)设置与运行
cp -r /www/code/python-talk/deployment/common /www
cd /www/common/
docker compose -f docker-compose-common.yml up -d

# 后端(python_talk)设置与运行
mkdir -p /www/backend/python_talk
cp -r /www/code/python-talk/backend/ /www/backend/python_talk/
cd /www/backend/python_talk/backend
docker build -t python_talk:0.0.1 /www/backend/python_talk/backend
docker compose -f /www/backend/python_talk/backend/docker-compose.yml up -d

```

