from time import sleep


def test_successful_login_with_valid_creds(login_page, valid_creds):
    login_page.open()
    login_page.fill_username_field(valid_creds["standard_user_username"])
    login_page.fill_password_field(valid_creds["password"])
    login_page.click_submit_button()
    sleep(5)