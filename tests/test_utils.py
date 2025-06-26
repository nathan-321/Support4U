from unittest.mock import MagicMock, patch
import pytest
from flask_login import current_user
from tests.setup_test_users import example_login_admin_user, example_login_user
from utils.utils import displaying_error, encypt_password, admin_logged_in

def test_encrypt_password():
    inputted_password = "hello"
    hashed_password = encypt_password(inputted_password)
    assert hashed_password != inputted_password


# def test_display_error():
#     test_database_error = "Error 405: Database has been deleted"
#     response = displaying_error(test_database_error)
#     assert b'Error! Unable to perform actions, see logger for more info!' in response.data
