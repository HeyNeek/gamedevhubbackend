from db import db

class DevModel(db.Model):
    __tablename__ = "devs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    projects = db.relationship("ItemModel", back_populate="dev")
    
    #idea!!! Maybe dev table should own multiple Users since a studio is comprised of many people. 
    #also probably add a owner/owners column for people who can do admin shit
    members = db.relationship("UserModel", back_populate="teams")