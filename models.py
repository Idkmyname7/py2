from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    method = db.Column(db.String(10))
    url = db.Column(db.String(500))
    status = db.Column(db.Integer)
    size = db.Column(db.Integer)
