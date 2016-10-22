from flask import request, jsonify
from src.main import app
from src.main import db

@app.route("/v1/healthcheck", methods = ['GET'])
def healthcheck():
    ok = True
    db = True

    try:
        users = User.query.first()
    except:
        ok = False
        db = False

    return jsonify(ok = ok, db = db)
