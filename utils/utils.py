from flask import current_app, request, flash
from flask_login import current_user
import hashlib

# Ensures password is encrypted before storing in database
def encypt_password(password):
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return hashed_password

# Ensures user is an admin
def admin_logged_in():
    if not current_user.account_type_admin:
        flash('You must be admin to access this page!', 'error')
        return False
    return True

# Gets the login details and returns in a dictionary
# Made the email optional as when logging in the user doesn't require an email
def request_user_details():
    inputted_username = request.form['username']
    inputted_email = request.form.get('email')
    inputted_password = encypt_password(request.form['password'])
    return({"username": inputted_username, "email": inputted_email, "password": inputted_password})

# Displays and logs the database error
def displaying_error(db_error):
    current_app.logger.error(f"Error: {db_error}")
    return(flash('Error! Unable to perform actions, see logger for more info!', 'error'))
