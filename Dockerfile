FROM python:3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app 

COPY ./reservation_system /app

WORKDIR /app