from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from v1 import create_v1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

app.register_blueprint(create_v1(db))

def init():
    """Initializes the application"""
    print "Initializing the database: %s" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"

init()
