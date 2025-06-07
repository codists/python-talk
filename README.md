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
# How to run Celery
**Note:** If you use rabbitmq or redis, and so on, please start they before starting Celery.
```shell
python-talk/backend$ celery -A python_talk.entrypoint.celery worker -l info

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


