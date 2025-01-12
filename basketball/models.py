from db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    favorite_team = db.Column(db.String(150))
    age = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean, default=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_neutral = db.Column(db.String(150))
    vpts = db.Column(db.Integer)
    home_neutral = db.Column(db.String(150))
    hpts = db.Column(db.Integer)
