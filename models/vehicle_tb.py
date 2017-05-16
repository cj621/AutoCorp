from main import db
from datetime import datetime
from flask_login import UserMixin

class Vehicle(UserMixin, db.Model):
	__tablename__ = 'vehicle'
	id = db.Column(db.Integer, primary_key=True)
	v_no = db.Column(db.String(20), unique=True, nullable=False)
	owner_name = db.Column(db.String(200), nullable=False)
	type_of_vehicle = db.Column(db.String(50), nullable=False)
	owner_mobile_no = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime(timezone=False), default=datetime.now(), nullable=False)