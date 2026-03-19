from setup_test_users import example_login_user, example_register_user

# Creates tests on registering users and logging in users
# Happy paths
def test_success_register_new_user(client):
    response = example_register_user(client)
    assert b'Account created! Please login:' in response.data
    
def test_success_register_same_user(client):
    example_register_user(client)
    response = example_register_user(client)
    assert b'Your account already exists!' in response.data

def test_success_login_new_user(client):
    example_register_user(client)
    response = example_login_user(client)
    assert b'Login successful! Hello, Regular!' in response.data

def test_logout(client):
    example_login_user(client)
    response = client.get('/logout', follow_redirects=True)    
    assert b'Logged out successfully!' in response.data

# Sad paths

def test_invalid_login_incorrect_username(client):
    response = client.post('/login', data={
        'username': 'invalid',
        'password': 'password123'
    }, follow_redirects=True)

    assert b'Incorrect username or password! Please try again.' in response.data

def test_invalid_login_incorrect_password(client):
    response = client.post('/login', data={
        'username': 'Regular',
        'password': '123'
    }, follow_redirects=True)

    assert b'Incorrect username or password! Please try again.' in response.data

def test_invalid_register_duplicate_account(client):
    example_register_user(client)
    response = client.post('/register', data={
        'username': 'Regular',
        'email': 'regular@email.com',
        'password': 'thisispassword123'
    }, follow_redirects=True)

    assert b'Your account already exists!' in response.data

# Security paths

def test_SQL_injection(client):
    response = client.post('/login', data={
        'username': "' OR 1=1 --",
        'password': 'password123'
    }, follow_redirects=True)

    assert b'Incorrect username or password! Please try again.' in response.data

