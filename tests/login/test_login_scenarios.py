import dotenv
import pytest
from pages.login.login_page import LoginPage

dotenv.load_dotenv()

def test_successful_login_with_valid_creds(
    login_page,
    valid_creds
):
    login_page.open()
    login_page.fill_username_field(valid_creds["standard_user_username"])
    login_page.fill_password_field(valid_creds["password"])
    inventory_page = login_page.click_submit_button()

    assert inventory_page.is_inventory_visible()

@pytest.mark.parametrize("username_key, is_username_valid, password_key, is_password_valid, expected_error_key", [
    ("standard_user_username", False, "password", True, "invalid_username"),
    ("standard_user_username", True, "password", False, "invalid_password"),
    ("standard_user_username", False, "password", False, "invalid_username_and_password"),

    (None, False, "password", True, "empty_username"),
    ("standard_user_username", True, None, False, "empty_password"),
    (None, False, None, False, "empty_username_and_password")
])
def test_login(
        login_page,
        valid_creds,
        invalid_creds,
        error_messages_data,
        username_key,
        is_username_valid,
        password_key,
        is_password_valid,
        expected_error_key
):
    if username_key is None:
        username = ""
    elif is_username_valid:
        username = valid_creds["standard_user_username"]
    else:
        username = invalid_creds["standard_user_username"]

    if password_key is None:
        password = ""
    elif is_password_valid:
        password = valid_creds["password"]
    else:
        password = invalid_creds["password"]

    login_page.open()
    if username:
        login_page.fill_username_field(username)
    if password:
        login_page.fill_password_field(password)
    login_page.click_submit_button()

    expected_error = error_messages_data[expected_error_key]

    assert login_page.get_error_text() == expected_error

def test_logout_after_successful_login(auth_inventory_page):
    auth_inventory_page.header.click_burger_menu_button()
    auth_inventory_page.sidebar.click_logout_button()

    login_page = LoginPage(auth_inventory_page.driver)

    assert login_page.is_login_logo_visible()