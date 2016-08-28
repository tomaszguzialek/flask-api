from flask import Blueprint, request, jsonify
from . import v1

def create_v1(db):
    v1 = Blueprint('v1', __name__)

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

    @v1.route("/v1/feature_request", methods = ['GET', 'POST'])
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

    return v1
