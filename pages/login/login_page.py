from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = ""

    def fill_username_field(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
