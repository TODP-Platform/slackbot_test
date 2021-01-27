from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PickCard(db.Model):
    __tablename__ = 'cardhistory'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(16))
    card_subject = db.Column(db.String(32))
    card_number = db.Column(db.Integer)
    card_status = db.Column(db.Integer)
