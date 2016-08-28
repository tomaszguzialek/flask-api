from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

from src.v1 import feature_request_controller

def init():
    """Initializes the application"""
    print "Initializing the database: %s" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"

init()
