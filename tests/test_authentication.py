from tests.setup_test_users import example_login_user
from tests.test_tickets import example_regular_user_post_ticket

# Ensures authentication is setup so that any user can't access certain pages.

def test_require_login(client):
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 405

def test_directs_to_login_page(client):
    response = client.get('/', follow_redirects=True)
    assert b'Login' in response.data

def test_access_denied_delete_ticket(client):
    example_regular_user_post_ticket(client)
    response = client.get('/delete-ticket/1', follow_redirects=True)    
    assert response.status_code == 403

def test_access_denied_promote_user(client):
    example_login_user(client)
    response = client.get("/promote-user/1", follow_redirects=True)
    assert response.status_code == 403

def test_access_denied_view_all_users(client):
    example_login_user(client)
    response = client.get("/users", follow_redirects=True)
    assert response.status_code == 403