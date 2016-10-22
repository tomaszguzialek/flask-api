from collections import OrderedDict
from flask import request, jsonify
from src.main import app
from src.models.user import User

import json

@app.route("/v1/healthcheck", methods = ['GET'])
def healthcheck():
    ok = True
    db = True

    try:
        userCount = User.query.count()
    except:
        db = False
        everything = False

    return json.dumps(OrderedDict([("everything", ok), ("db", db)]))
