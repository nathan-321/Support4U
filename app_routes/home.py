from flask import Blueprint, render_template
from models.models import Ticket

home_blueprint = Blueprint('home', __name__)

# Runs index.html and passes tickets through
@home_blueprint.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)