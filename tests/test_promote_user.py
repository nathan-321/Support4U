import pytest

from tests.setup_test_tickets import example_regular_user_post_ticket
from tests.setup_test_users import example_login_admin_user, example_login_admin_user, example_register_user


def promote_user(client):
    example_register_user(client)
    example_login_admin_user(client)
    
    response = client.post('/promote-user/1', follow_redirects=True)
    assert b'chocolate' in response.data

def demote_user(client):
    example_login_admin_user(client)
    example_login_admin_user(client)

    response = client.post('/promote-user/1', follow_redirects=True)
    assert b'Regular has been demoted to a regular user!' in response.data



