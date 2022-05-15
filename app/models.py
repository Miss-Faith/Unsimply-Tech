from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

class Quote:
    '''
    Quote class to define quotes
    '''

    all_quotes = []

    def __init__(self,author,id,quote):
        self.author = author
        self.id = id
        self.quote = quote

    def save_quote(self):
        Quote.all_quotes.append(self)

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True,index = True)
    email = db.Column(db.String(255),unique = True,index = True)

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    secure_password = db.Column(db.String(255),nullable = False)

    quotes = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'