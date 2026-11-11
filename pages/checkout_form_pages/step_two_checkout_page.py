from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.checkout_form_pages.base_checkout_page import BaseCheckoutPage


class CheckoutPageStepTwo(BaseCheckoutPage):
    FINISH_BUTTON = (By.ID, 'finish')
    TOTAL_SUM_LABEL = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.endpoint = 'checkout-step-two.html'

    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)

    def get_total_sum(self):
        unformatted = self.get_text(self.TOTAL_SUM_LABEL)

        return unformatted.replace('Total: ', '').replace('$', '')