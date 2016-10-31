# flask-api [![Build Status](https://travis-ci.org/tomaszguzialek/flask-api.svg?branch=master)](https://travis-ci.org/tomaszguzialek/flask-api)
RESTful API in Python with Flask.

## Build
```
pip install -r requirements.txt
```

## Deploy

### Manual deployment
Recommended server to deploy is Gunicorn:
```
pip install gunicorn
gunicorn -b 0.0.0.0:5000 src.runner:app
```

### Docker container deployment
In order to build a docker container from local repository state:
```
docker build -t tomaszguzialek/flask-api .
```

The repository contains also ```docker-compose.yml``` file spinning up tomaszguzialek/flask-api container together with a MySQL container.

### Fabric deployment
Also, a Fabric file is provided that orchestrates deployment of the master branch on a remote Ubuntu machine via SSH. A test Ubuntu virtual machine can be brought up via Vagrantfile:
```
cd deployment/vagrant-test-server
vagrant up
cd ..
fab -H localhost:2222 -u vagrant -p vagrant deploy
```

## Configuration
By default, the app initializes SQLite database in ```/tmp/flask-api.db``` and adds sample data at startup (see src/conf/flask_api_conf.py for configuration file). The configuration file can be overriden by a file set in FLASK_API_CONF environmental variable. Also, individual keys can be tuned via environmental variables (with FLASK_API_ prefix), e.g. INIT_SAMPLE_DATA can be set via ```export FLASK_API_INIT_SAMPLE_DATA=False```

### Docker configuration
In order to run docker container with adjusted configuration:
```
docker run -d -p 5000:5000 tomaszguzialek/flask-api -e FLASK_API_INIT_SAMPLE_DATA=False
```

## Tests
In order to run the tests:
```
python -m unittest discover
```
