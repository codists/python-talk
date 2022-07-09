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
backend$ cd python_talk/
backend/python_talk$ export FLASK_APP=entrypoint
backend/python_talk$ flask run
```
# How to run Celery
```python
backend/python_talk$ celery -A entrypoint.celery worker -l info

```
# How to run frontend

Todo
