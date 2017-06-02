from main import app, db, login_manager
from flask import Flask, request, url_for, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from models.police_tb import *

login_manager.login_view = '/' #this works with @login_required decorator
login_manager.login_message = 'You need to log in with correct credentials!'


## mapping the python flask object with the object in the actual model
@login_manager.user_loader
def load_user(user_id):
	uid = Police.query.get(user_id)
	return uid


@app.route('/')
def login():
	return render_template("login.html")


@app.route('/loggedin', methods = ['POST'])
def loggedin():
	id = request.form['id']
	password = request.form['password']

	police = Police.query.filter_by(police_id = id).first()

	if not police:
		flash('User Not Found! Please contact your Branch Head.')
		return redirect(url_for('login'))
	elif police.password != password:
		flash('Invalid Credentials!')
		return redirect(url_for('login'))
	else:
		login_user(police)
		return redirect(url_for('home'))



@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Successfully Logged Out!')
	return redirect(url_for('login'))



@app.route('/home')
@login_required
def home():
	return render_template("police_home.html", current_user = current_user)
