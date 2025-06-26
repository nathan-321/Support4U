from flask import Flask
from models.models import db, User
from dotenv import load_dotenv
from flask_login import LoginManager
from app_routes.account import account_blueprint
from app_routes.tickets import ticket_blueprint
from app_routes.promote_user import promote_user_blueprint
from app_routes.home import home_blueprint
import os

login_manager = LoginManager()
@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))


def setup_app(test_config=False):

    load_dotenv()

    # Creates app
    app = Flask(__name__)    
    app.register_blueprint(account_blueprint)
    app.register_blueprint(ticket_blueprint)
    app.register_blueprint(promote_user_blueprint)
    app.register_blueprint(home_blueprint)

    app.secret_key = os.getenv('SECRET_KEY')

    # If testing, it will create a seperate database
    if test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TESTING')
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Creates Databases
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Enables Flask-Login to ensure users must be logged in to view certain pages 
    login_manager.init_app(app)
    login_manager.login_view = "account.login"

    return app