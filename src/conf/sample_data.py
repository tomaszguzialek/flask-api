from src.models.user import User
from src.models.client import Client
from src.models.feature_request import FeatureRequest

from src.main import db

def init_users():
    print "Pre-populating users"
    user_tomasz = User("tomasz", "admin_obviously")
    db.session.add(user_tomasz)
    db.session.commit()
    print "Users populated"

def init_clients():
    print "Pre-populating clients"
    client_a = Client("A")
    db.session.add(client_a)
    client_b = Client("B")
    db.session.add(client_b)
    db.session.commit()
    print "Clients populated"

def init_feature_requests():
    print "Pre-populating feature requests"
    fr1 = FeatureRequest("title 1", "description 1", 1)
    db.session.add(fr1)
    fr2 = FeatureRequest("title 2", "description 2", 2)
    db.session.add(fr2)
    fr3 = FeatureRequest("title 3", "description 3", 1)
    db.session.add(fr3)
    db.session.commit()
    print "Feature request populated"
