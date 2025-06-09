# python-talk
Using Python + Flask  + Vue + Axios + JWT to build a forum.

# How to run backend

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
# How to run frontend
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

# How to deploy project in production?

- **Deployment Structure**

考虑到有多个应用的场景，同时为了保证部署的可扩展性，采用下面的部署结构。项目部署到 /www 目录下。

```├── backend
