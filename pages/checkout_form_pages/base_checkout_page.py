from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BaseCheckoutPage(BasePage):
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)
