#FROM python:3.8-slim-buster
FROM hub.hamdocker.ir/python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Install libgl1-mesa-glx
#RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app/