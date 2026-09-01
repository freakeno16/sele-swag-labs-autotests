import os
import pytest
from pages.login.login_page import LoginPage
import dotenv

dotenv.load_dotenv()

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def valid_creds():
    valid_creds = {
        "standard_user_username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
    }
    return valid_creds