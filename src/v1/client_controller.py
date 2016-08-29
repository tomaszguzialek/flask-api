from flask import request, jsonify
from src.main import app
from src.main import db
from src.models.client import Client

@app.route("/v1/client", methods = ['GET', 'POST'])
def clients():
    if request.method == 'POST':
        body = request.get_json()
        return add_client(body['name'])
    return get_all_clients()

def get_all_clients():
    clients = Client.query.all();
    return jsonify(clients = [client.jsonify() for client in clients])

def add_client(name):
    client = Client(name)
    db.session.add(client)
    db.session.commit()
    return '', 201
