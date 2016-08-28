from src.main import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Client %s>' % self.name

    def jsonify(self):
       """Return JSON representation of the object"""
       return {
           'id' : self.id,
           'name': self.name
       }
