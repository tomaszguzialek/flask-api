from flask import request, jsonify
from src.main import app
from src.main import db
from src.models.client import Client
from src.models.user import User

@app.route("/v1/auth/login", methods = ['POST'])
def login():
    body = request.get_json()
    app.logger.info(body)
    if body['login'] is None:
        return '', 403

    user = User.query.filter_by(login = body['login']).first()
    if user is None:
        return '', 403

    if user.password != body['password']:
        return '', 403

    return jsonify(user = user.jsonify())

def get_all_clients():
    clients = Client.query.all();
    return jsonify(clients = [client.jsonify() for client in clients])

def add_client(name):
    client = Client(name)
    db.session.add(client)
    db.session.commit()
    return '', 201
