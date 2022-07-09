# python-talk
Using Python + Flask  + Vue + Axios + JWT to build a forum.

# How to run backend

- clone

```python
$ git clone https://github.com/codists/python-talk.git
```

- create and activate virtual environment

```python
$ cd python-talk/backend/
backend$ source ./venv/bin/activate
```

- install requirements.txt

```python
python-talk/backend$ pip install -r requirements.txt
```

- run 

```python
backend/$ flask run
```
# How to run Celery
```python
backend/$ celery -A python_talk.entrypoint.celery_app worker -l info

```
# How to run frontend

Todo
