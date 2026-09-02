import os
import pytest
import dotenv
from test_data.login.error_messages import error_messages

dotenv.load_dotenv()

@pytest.fixture
def valid_creds():
    valid_creds = {
        "standard_user_username": os.getenv("STANDARD_USER_USERNAME"),
        "password": os.getenv("PASSWORD"),
    }
    return valid_creds

@pytest.fixture
def invalid_creds():
    invalid_creds = {
        "standard_user_username": os.getenv("INVALID_STANDARD_USER_USERNAME"),
        "password": os.getenv("INVALID_PASSWORD"),
    }
    return invalid_creds

@pytest.fixture
def error_messages_data():
    return error_messages