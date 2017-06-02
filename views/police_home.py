from main import app, db, login_manager
from flask import Flask, request, url_for, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from random import randint
from twilio.rest import Client



@app.route('/send_sms', methods = ['POST'])
@login_required
def send_sms():
	ph_no = request.form['phone']
	if len(ph_no) != 10:
		flash('The entered phone number was inaccurate. Please check the number of digits entered')
		return redirect(url_for('home'))
	else:
		ph_no = int(ph_no)
		otp = randint(67890, 99999)
		session[current_user.police_id+'_otp'] = otp
		print(session[current_user.police_id+'_otp'])
		# Account SID from twilio.com/console
		account_sid = app.config['TWILIO_ACCOUNT_SID']
		# Auth Token from twilio.com/console
		auth_token = app.config['TWILIO_AUTH_TOKEN']
		
		client = Client(account_sid, auth_token)
		message = client.messages.create(
			to="+919513138311",
			from_="+13525770269",
			body="OTP for AutoCorp Validation! : "+ str(otp))

		flash('OTP Sent via SMS')
		return redirect(url_for('home'))


@app.route('/verify_otp', methods=['POST'])
@login_required
def verify_otp():
	if not request.form['otp']:
		flash('OTP input cannot be blank')
		return redirect(url_for('home'))
	else:
		inserted_otp = int(request.form['otp'])
	
	if  not current_user.police_id+'_otp' in session:
		flash('The OTP was used previously. Cannot be used twice. Generate another OTP.')
		return redirect(url_for('home'))
	else:
		if inserted_otp == session[current_user.police_id+'_otp']:
			session.pop(current_user.police_id+'_otp', None)
			return redirect(url_for('rule_break'))
		else:
			flash('Entered OTP is invalid')
			return redirect(url_for('home'))


@app.route('/home/rule_break')
@login_required
def rule_break():
	return render_template('rule_break.html', current_user = current_user)
	
