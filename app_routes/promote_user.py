from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.models import db, User
from utils.utils import admin_logged_in

promote_user_blueprint = Blueprint('promote_user', __name__)

# Displays promote users page with all users as parameters
@promote_user_blueprint.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('promote_user.html', users=users)


# Allows admin to promote/demote a specific user
@promote_user_blueprint.route('/promote-user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def promote_user(user_id):
    if not admin_logged_in():
        return redirect(url_for('home.index'))
    
    user = db.session.query(User).filter_by(user_id=user_id).first()

    if request.method == 'POST':
        user.account_type_admin = not(user.account_type_admin)
        try:
            db.session.commit()
            if user.account_type_admin:
                flash(f'{user.username} is now admin!', 'success')
            else:
                flash(f'{user.username} has been demoted to a regular user!', 'success')

        except Exception as db_error:
            current_app.logger.error(f"Database error: {db_error}")
            
        
    return redirect(url_for('promote_user.users'))