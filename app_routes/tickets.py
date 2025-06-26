from flask import Blueprint, Flask, current_app, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models.models import db, Ticket
from utils.utils import admin_logged_in, displaying_error

ticket_blueprint = Blueprint('tickets', __name__)

# Displays new ticket form and submits the new ticket to the tickets table if the form is completed
@ticket_blueprint.route('/submit-ticket', methods=['GET','POST'])
@login_required
def submit_ticket():
    if request.method == 'POST':
        
        ticket = Ticket(title=request.form['title'], 
                        description = request.form['description'],
                        priority = request.form['priority'],
                        status = request.form['status'],
                        ticket_creator_id = current_user.user_id)
        
        try:
            db.session.add(ticket)
            db.session.commit()
            flash('Ticket submitted successfully!', 'success')
            return redirect(url_for('home.index'))
        
        except Exception as db_error:
            displaying_error(db_error)
        
    return render_template('new_ticket.html')

# Updates the specific ticket with the updated values
@ticket_blueprint.route('/edit-ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(ticket_id):
    ticket = db.session.query(Ticket).filter_by(ticket_id=ticket_id).first()

    if (current_user.account_type_admin == False) and ticket.ticket_creator_id != current_user.user_id:
        flash('You are not authorized to edit this ticket!', 'error')
        current_app.logger.warning("You are not authorized to edit this ticket!")
        return redirect(url_for('home.index'))
    
    if request.method == 'POST':
        ticket.title = request.form['title']
        ticket.description = request.form['description']
        ticket.priority = request.form['priority']
        ticket.status = request.form['status']
        try:
            db.session.commit()
            flash('Ticket updated successfully!', 'success')
            return redirect(url_for('home.index'))
        except Exception as db_error:
            displaying_error(db_error)
        

    return render_template('edit_ticket.html', ticket=ticket)

# Allows admin to delete a ticket
@ticket_blueprint.route('/delete-ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def delete_ticket(ticket_id):
    if (admin_logged_in() == False):
        return redirect(url_for('home.index'))
    
    ticket = db.session.query(Ticket).filter_by(ticket_id=ticket_id).first()
    try:
        db.session.delete(ticket)
        db.session.commit()
        flash('Ticket deleted successfully!', 'success')
    except Exception as db_error:
        displaying_error(db_error)

    return redirect(url_for('home.index'))
