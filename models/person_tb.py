from main import db
from datetime import datetime
from flask_login import UserMixin

class Person(UserMixin, db.Model):
	__tablename__ = 'person'
	id = db.Column(db.Integer, primary_key=True)
	lc_no = db.Column(db.String(20), unique=True, nullable=False)
	name = db.Column(db.String(200), nullable=False)
	date_of_issue = db.Column(db.DateTime(timezone=False), nullable=False)
	valid_upto = db.Column(db.DateTime(timezone=False), nullable=False)
	dob = db.Column(db.Date, nullable=False)
	address = db.Column(db.String(500), nullable=False)
	mobile_no = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime(timezone=False), default=datetime.now(), nullable=False)