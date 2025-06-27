from models.models import User, db
from utils.utils import encypt_password

# Creates a regular user
def example_register_user(client):
    return client.post('/register', data={
        'username': 'Regular',
        'email': 'regular@email.com',
        'password': 'password123'
    }, follow_redirects=True)

# Creates and logs in regular user
def example_login_user(client):
    example_register_user(client)
    return client.post('/login', data={
        'username': 'Regular',
        'password': 'password123'
    }, follow_redirects=True)

# Creates a admin user
def create_admin_user():
    user = User(
        username="Admin",
        email="admin@email.com",
        password=encypt_password("password123"),
        account_type_admin=True  # or however you mark admin
    )
    db.session.add(user)
    db.session.commit()
    return user

# Creates and logs in admin user
def example_login_admin_user(client):
    create_admin_user()
    return client.post('/login', data={
        'username': 'Admin',
        'password': 'password123'
    }, follow_redirects=True)

