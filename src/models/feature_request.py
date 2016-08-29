from src.main import db

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(120))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable = False)
    client = db.relationship("Client", back_populates = "feature_requests")

    def __init__(self, title, description, client_id):
        self.title = title
        self.description = description
        self.client_id = client_id

    def __repr__(self):
        return '<FeatureRequest %s>' % self.title

    def jsonify(self):
       """Return JSON representation of the object"""
       return {
           'id' : self.id,
           'title': self.title,
           'description': self.description,
           'client_id': self.client_id
       }
