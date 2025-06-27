from tests.setup_test_users import example_login_admin_user, example_login_user

# These functions reduces repeatbility in the tests. 
# These login the user and submits an example ticket

def example_regular_user_post_ticket(client):
    example_login_user(client)
    return(client.post('/submit-ticket', data={
        'title': 'Reset Password',
        'description': 'I need to reset my Microsoft email',
        'priority': '3',
        'status': 'Open'
    }, follow_redirects=True))

def example_admin_post_ticket(client):
    example_login_admin_user(client)
    return(client.post('/submit-ticket', data={
        'title': 'Reset Password',
        'description': 'I need to reset my Microsoft email',
        'priority': '3',
        'status': 'Open'
    }, follow_redirects=True))