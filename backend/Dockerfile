FROM python:3.10

ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt /app/requirements.txt
COPY python_talk /app

WORKDIR /app

RUN pip install -r requirements.txt -i  https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
