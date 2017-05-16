from main import db
from datetime import datetime
from flask_login import UserMixin

class Rules(UserMixin, db.Model):
	__tablename__ = 'rules'
	id = db.Column(db.Integer, primary_key=True)
	rule_no = db.Column(db.Integer, unique=True, nullable=False)
	statement = db.Column(db.String(500), nullable=False)
	action = db.Column(db.String(200), nullable=False)
	severity = db.Column(db.String(10), nullable=False)
	created_at = db.Column(db.DateTime(timezone=False), default=datetime.now(), nullable=False)