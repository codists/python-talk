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

```

## 部署流程

一般来说，部署时是不需要拉取代码仓库的，前端直接上传 dist 目录，后端直接上传代码即可。这里这样做是为了让不熟悉该流程的人更好的理解。

```
# 目录设置
mkdir -p /www/backend/python_talk
mkdir -p /www/frontend/python_talk

# 拉取代码
cd /www/temp
git clone https://github.com/codists/python-talk.git

# 前端(frontend)设置
cd /www/temp/python-talk/frontend
npm install
npm run build # 得到一个 dist 目录
cp /www/temp/python-talk/frontend/dist /www/frontend/python_talk/

# 公共应用(mysql, redis, nginx)设置及启动
cp -r /www/temp/python-talk/deployment/common /www
cd /www/common/
# docker compose -f docker-compose-common.yml up -d

# 后端(python_talk)设置及启动
cp -r /www/temp/python-talk/backend/ /www/backend/python_talk/
cd /www/backend/python_talk/backend
docker compose up -d

```

