# flask-api
RESTful API in Python with Flask.

## Build
```
pip install -r requirements.txt
```

## Deploy
Recommended server to deploy is Gunicorn:
```
pip install gunicorn
gunicorn -b 0.0.0.0:8000 src.runner:app
```

Also, a Fabric file is provided that orchestrates deployment of the master branch on a remote Ubuntu machine via SSH. A test Ubuntu virtual machine can be brought up via Vagrantfile:
```
cd deployment/vagrant-test-server
vagrant up
cd ..
fab -H localhost:2222 -u vagrant -p vagrant deploy
```

## Database
By default, the app initializes SQLite database in ```/tmp/flask-api.db``` and adds sample data at startup. Remember to remove the DB file to start fresh.

## Tests
In order to run the tests:
```
python -m unittest discover
```
