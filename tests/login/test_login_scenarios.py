def test_successful_login_with_valid_creds(login_page, valid_creds, inventory_page):
    login_page.open()
    login_page.fill_username_field(valid_creds["standard_user_username"])
    login_page.fill_password_field(valid_creds["password"])
    login_page.click_submit_button()
    inventory_page.check_inventory_is_visible()


def test_unsuccessful_login_with_invalid_username(
    login_page,
    invalid_creds,
    valid_creds,
    error_messages_data
):
    login_page.open()
    login_page.fill_username_field(invalid_creds["standard_user_username"])
    login_page.fill_password_field(valid_creds["password"])
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["invalid_username"])

def test_unsuccessful_login_with_invalid_password(
    login_page,
    invalid_creds,
    valid_creds,
    error_messages_data
):
    login_page.open()
    login_page.fill_username_field(valid_creds["standard_user_username"])
    login_page.fill_password_field(invalid_creds["password"])
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["invalid_password"])

def test_unsuccessful_login_with_invalid_username_and_password(
    login_page,
    invalid_creds,
    error_messages_data
):
    login_page.open()
    login_page.fill_username_field(invalid_creds["standard_user_username"])
    login_page.fill_password_field(invalid_creds["password"])
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["invalid_username_and_password"])

def test_unsuccessful_login_with_empty_username(
    login_page,
    valid_creds,
    error_messages_data
):
    login_page.open()
    login_page.fill_password_field(valid_creds["password"])
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["empty_username"])

def test_unsuccessful_login_with_empty_password(
    login_page,
    valid_creds,
    error_messages_data
):
    login_page.open()
    login_page.fill_username_field(valid_creds["standard_user_username"])
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["empty_password"])

def test_unsuccessful_login_with_empty_username_and_password(
    login_page,
    error_messages_data
):
    login_page.open()
    login_page.click_submit_button()
    login_page.check_error_message(error_messages_data["empty_username_and_password"])