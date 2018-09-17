FROM python:3.6

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app/
