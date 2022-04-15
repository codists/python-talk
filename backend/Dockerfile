FROM python:3.10.4-slim

ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt /app/requirements.txt
COPY python_talk /app

WORKDIR /app

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

CMD ["python", "entrypoint.py"]
