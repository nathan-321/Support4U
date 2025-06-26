from conftest import app
import pytest
from models.models import Ticket, User, db
from tests.setup_test_tickets import example_admin_post_ticket, example_regular_user_post_ticket
from tests.setup_test_users import example_login_admin_user


def test_regular_user_submit_ticket(client):
    response = example_regular_user_post_ticket(client)
    assert response.status_code == 200
    assert b'Ticket submitted successfully!' in response.data
    assert b'Reset Password' in response.data

def test_admin_submit_ticket(client):
    response = example_admin_post_ticket(client)
    assert response.status_code == 200
    assert b'Ticket submitted successfully!' in response.data
    assert b'Reset Password' in response.data

def test_view_ticket(client):
    example_regular_user_post_ticket(client)
    response = client.get('/', follow_redirects=True)

    assert response.status_code == 200
    assert b'Reset Password' in response.data

def test_success_edit_ticket(client):
    example_regular_user_post_ticket(client)
    response = client.post('/edit-ticket/1', data={
        'title': 'Reset Password',
        'description': 'I need to reset my Microsoft email',
        'priority': '3',
        'status': 'Resolved'
    }, follow_redirects=True)    

    assert response.status_code == 200
    assert b'Resolved' in response.data

def test_success_delete_ticket(client):
    example_admin_post_ticket(client)
    response = client.post('/delete-ticket/1', follow_redirects=True)
    print(response.data)
    assert b'Ticket deleted successfully!' in response.data

# def demote_user(client):
#     example_login_admin_user(client)
#     example_regular_user_post_ticket(client)
#     example_login_admin_user(client)

#     response = client.post('/delete-ticket/1', follow_redirects=True)
#     assert 'Regular has been demoted to a regular user!' in response.data