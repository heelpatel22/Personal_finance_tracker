from models import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200),nullable=False)
    category = db.Column(db.String(100),nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'<Transaction  {self.amount}>'