from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import current_user, login_required, login_user, logout_user
from models.models import db, User
from utils.utils import displaying_error, password_requirements_and_encryption, request_user_details

account_blueprint = Blueprint('account', __name__)

# Allows users to create a new account (regular) and adds it to the User database table
@account_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if password_requirements_and_encryption():
            user_details = password_requirements_and_encryption()
        else:
            flash("Your password doesn't meet the requirements!", 'error')
            return redirect(url_for('account.register'))
        
        if len(user_details["username"]) > 15:
            flash("Your username doesn't meet the requirements!", 'error')
            return redirect(url_for('account.register'))

        account_exists = User.query.filter_by(email=user_details["email"]).first()
        if account_exists:
            flash('Your account already exists!', 'error')
            return redirect(url_for('account.register'))
        
        # There is frontend validation to ensure that all fields are provided and the email is an email address
        user = User(username=user_details["username"], email=user_details["email"], password=user_details["password"])
        try:
            db.session.add(user)
            db.session.commit()
            flash('Account created! Please login:', 'success')
            return redirect(url_for('home.index'))
        except Exception as db_error:
            displaying_error(db_error)
    
    return render_template('register.html')

# Checks if login info matches users database and grants access if matched
@account_blueprint.route('/login', methods=['POST'])
def login():
    user_details = request_user_details()
    user = User.query.filter_by(username=user_details["username"]).first()
    
    if user and user.password == user_details["password"]:
        login_user(user)
        flash(f'Login successful! Hello, {current_user.username}! ', 'success')
    else:
        current_app.logger.warning("Unsuccessful login attempt!")
        flash('Incorrect username or password! Please try again.', 'error')

    return redirect(url_for('home.index'))

# Logs out user in the session 
@account_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home.index'))