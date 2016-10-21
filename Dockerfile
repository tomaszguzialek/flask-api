FROM ubuntu:16.04

MAINTAINER Tomasz Guzialek "tomasz@guzialek.info"

RUN apt-get update -y \
    && apt-get install -y \
    gunicorn \
    python-dev \
    python-pip \
    && rm -rf /var/lib/apt/lists/*

COPY . /flask-api

WORKDIR /flask-api

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b 0.0.0.0:5000", "src.runner:app"]

EXPOSE 5000
