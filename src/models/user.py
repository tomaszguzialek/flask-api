from sqlalchemy_utils import PasswordType, force_auto_coercion
from src.main import db

force_auto_coercion()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable = False)
    password = db.Column(PasswordType(schemes = ['pbkdf2_sha512']), nullable = False)

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.login

    def jsonify(self):
       """Return JSON representation of the object"""
       return {
           'id' : self.id,
           'login': self.login
       }
