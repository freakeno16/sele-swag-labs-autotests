from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = ""

    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_submit_button()

    def fill_username_field(self, username):
        self.find(self.USERNAME_INPUT).send_keys(username)

    def fill_password_field(self, password):
        self.find(self.PASSWORD_INPUT).send_keys(password)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)

    def check_error_message(self, error_text):
        assert self.get_text(self.ERROR_MESSAGE) == error_text
