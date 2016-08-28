from app.app import db

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
