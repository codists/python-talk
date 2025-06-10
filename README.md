# About python-talk
Using Python + Flask  + Vue + Axios + JWT to build a forum.

# How to run backend in develop environment

- clone

```shell
git clone https://github.com/codists/python-talk.git
```

- create and activate virtual environment

```shell
cd python-talk/backend/
python3 -m venv venv
source ./venv/bin/activate
```

- install requirements.txt

```shell
pip install -r requirements.txt
```

- run 

```shell
cd python-talk/backend/
flask run
```
# How to run frontend in develop environment
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

# How to deploy project in production environment

Use Docker、Nginx、Ubuntu to deploy the project。

## project structure for deployment

Although python_talk is only one application， we have to consider the flexibility when we deploy it on multiple servers and scalability when we coordinate it with other applications, so the deployment directory structure likes the following：

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

## step-by-step guide

Generally, there's no need to pull the code repository during deployment — the frontend only needs to upload the `dist` directory, and the backend only upload the code. This approach is used here to help those unfamiliar with the process better understand it.

```
# pull code
mkdir -p /www/code
cd /www/code
git clone https://github.com/codists/python-talk.git

# frontend setting
mkdir -p /www/frontend/python_talk
cd /www/code/python-talk/frontend
npm install # if you doesn't install npm, install it with command "sudo apt install npm -y" 
npm run build # it will generate a dist directory
cp -r /www/code/python-talk/frontend/dist /www/frontend/python_talk/

# common applications(mysql, redis, nginx) setting and run
cp -r /www/code/python-talk/deployment/common /www
cd /www/common/
docker compose -f docker-compose-common.yml up -d

# backend(python_talk)setting and run
mkdir -p /www/backend/python_talk
cp -r /www/code/python-talk/backend/ /www/backend/python_talk/
cd /www/backend/python_talk/backend
docker compose up -d
```

