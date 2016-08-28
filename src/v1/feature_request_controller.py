from flask import Blueprint, request, jsonify
from src.main import app
from src.main import db
from src.models.feature_request import FeatureRequest

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
