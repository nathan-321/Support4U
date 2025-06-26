import sys
import pytest

sys.path.append('.')
sys.path.append('./__init')
sys.path.append('./models/models')

from __init__ import setup_app
from models.models import db

@pytest.fixture
def app():
    app = setup_app(test_config=True)
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()