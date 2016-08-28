from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/flask-api.db'

db = SQLAlchemy(app)

from src.v1 import feature_request_controller

def init_app():
    """Initializes the application"""
    print "Initializing the database: %s\n" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"
