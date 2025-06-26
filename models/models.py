from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

# Creates User table with flask login
class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    account_type_admin = db.Column(db.Boolean, default=False)
    def get_id(self):
        return str(self.user_id)

# Creates Ticket table
class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.Integer, default=3)
    status = db.Column(db.String(100), default="Open")
    date_time_created = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))
    ticket_creator_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    ticket_creator = db.relationship('User', backref='tickets')
