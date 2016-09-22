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
gunicorn src.main:app
```

## Database
By default, the app initializes SQLite database in ```/tmp/flask-api.db``` and adds sample data at startup. Remember to remove the DB file to start fresh.
