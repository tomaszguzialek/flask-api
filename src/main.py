from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from src.conf.app_config import app_config

app = Flask(__name__)
CORS(app)

app = app_config(app)

db = SQLAlchemy(app)

# Register controllers
from src.v1 import auth_controller
from src.v1 import feature_request_controller
from src.v1 import client_controller

def cleanup_invalidated_tokens():
    print "Starting background thread for cleaning up invalidated tokens"
    auth_controller.cleanup_invalidated_tokens()

def init_app():
    """Initializes the application"""
    print "Initializing the database: %s\n" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"

init_app()
if app.config['INIT_SAMPLE_DATA']:
    from src.conf import sample_data
    sample_data.init_users()
    sample_data.init_clients()
    sample_data.init_feature_requests()
