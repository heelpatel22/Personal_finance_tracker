from models import db

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    month = db.Column(db.String(10))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))