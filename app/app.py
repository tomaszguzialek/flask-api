from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(120))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<FeatureRequest %s>' % self.title

    def jsonify(self):
       """Return JSON representation of the object"""
       return {
           'id' : self.id,
           'title': self.title,
           'description': self.description
       }

def init():
    """Initializes the application"""
    print "Initializing the database: %s" % app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
    print "Database initialized"

@app.route("/v1/feature_request", methods = ['GET', 'POST'])
def feature_requests():
    if request.method == 'POST':
        body = request.get_json()
        return add_feature_request(body['title'], body['description'])
    return get_all_feature_requests()

def get_all_feature_requests():
    feature_requests = FeatureRequest.query.all();
    return jsonify(feature_requests = [feature_request.jsonify() for feature_request in feature_requests])

def add_feature_request(title, description):
    feature_request = FeatureRequest(title, description)
    db.session.add(feature_request)
    db.session.commit()
    return '', 201

init()
