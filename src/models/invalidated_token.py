from src.main import db
from sqlalchemy.sql import func

class InvalidatedToken(db.Model):
    token = db.Column(db.String(120), primary_key=True)
    invalidated_date = db.Column(db.DateTime(timezone = True), server_default = func.now())

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return '<InvalidatedToken %s, %s>' % (self.token, str(self.invalidated_date))

    def jsonify(self):
       """Return JSON representation of the object"""
       return {
           'token' : self.token,
           'invalidated_date': str(self.invalidated_date)
       }
