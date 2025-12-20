from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(300))  # URL or filename
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(300))  # URL or filename
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    designation = db.Column(db.String(100))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    city = db.Column(db.String(50))

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))

