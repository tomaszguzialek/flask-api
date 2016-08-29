from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/flask-api.db'

db = SQLAlchemy(app)

# Register models
from src.models.client import Client
# Register controllers
from src.v1 import auth_controller
from src.v1 import feature_request_controller
from src.v1 import client_controller

def init_clients():
    print "Pre-populating clients"
    client_a = Client("A")
    db.session.add(client_a)
    client_b = Client("B")
    db.session.add(client_b)
    db.session.commit()
    print "Clients populated"

def init_app():
    """Initializes the application"""
    print "Initializing the database: %s\n" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"
    init_clients()
