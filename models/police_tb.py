from main import db
from datetime import datetime
from flask_login import UserMixin

class Police(UserMixin, db.Model):
	__tablename__ = 'police'
	id = db.Column(db.Integer, primary_key=True)
	police_id = db.Column(db.String(50), unique=True, nullable=False)
	police_name = db.Column(db.String(200), nullable=False)
	branch = db.Column(db.String(100), nullable=False)
	mobile_no = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime(timezone=False), default=datetime.now(), nullable=False)