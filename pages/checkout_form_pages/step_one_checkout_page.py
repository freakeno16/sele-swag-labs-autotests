from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.checkout_form_pages.base_checkout_page import BaseCheckoutPage
from pages.checkout_form_pages.step_two_checkout_page import CheckoutPageStepTwo


class CheckoutPageStepOne(BaseCheckoutPage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.endpoint = 'checkout-step-one.html'

    def fill_firstname_field(self, firstname: str) -> None:
        self.type_text(self.FIRST_NAME_FIELD, firstname)

    def fill_lastname_field(self, lastname: str) -> None:
        self.type_text(self.LAST_NAME_FIELD, lastname)

    def fill_postal_code_field(self, postal_code: str) -> None:
        self.type_text(self.POSTAL_CODE_FIELD, postal_code)

    def click_continue_button(self) -> CheckoutPageStepTwo:
        self.click(self.CONTINUE_BUTTON)

        return CheckoutPageStepTwo(self.driver)
