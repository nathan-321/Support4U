from utils.utils import encypt_password

# This unit pytest test ensures that function encrypt password works 
# and that the password is encrypted to store in db

def test_encrypt_password():
    inputted_password = "hello"
    hashed_password = encypt_password(inputted_password)
    assert hashed_password != inputted_password

