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

RUN chmod +x wait-for-it.sh

RUN pip install -r requirements.txt

RUN if [ -z ${FLASK_API_CONF+x} ]; then export FLASK_API_CONF=${FLASK_API_CONF}; fi
RUN if [ -z ${FLASK_API_SQLALCHEMY_DATABASE_URI+x} ]; then export FLASK_API_SQLALCHEMY_DATABASE_URI=${FLASK_API_SQLALCHEMY_DATABASE_URI}; fi
RUN if [ -z ${FLASK_API_INIT_SAMPLE_DATA+x} ]; then export FLASK_API_INIT_SAMPLE_DATA=${FLASK_API_INIT_SAMPLE_DATA}; fi
RUN if [ -z ${FLASK_API_CLEANUP_INVALIDATED_TOKENS_INTERVAL_SECONDS+x} ]; then export FLASK_API_CLEANUP_INVALIDATED_TOKENS_INTERVAL_SECONDS=${FLASK_API_CLEANUP_INVALIDATED_TOKENS_INTERVAL_SECONDS}; fi

CMD ["gunicorn", "-b 0.0.0.0:5000", "-k gevent", "src.runner:app"]

EXPOSE 5000
