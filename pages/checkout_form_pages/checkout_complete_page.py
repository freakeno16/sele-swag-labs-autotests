from pages.checkout_form_pages.base_checkout_page import BaseCheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutCompletePage(BaseCheckoutPage):
    PONY_EXPRESS_LABEL = (By.CSS_SELECTOR, '[data-test="pony-express"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '[data-test="complete-text"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.endpoint = 'checkout-complete.html'

    def is_pony_express_label_visible(self) -> bool:
        return self.find(self.PONY_EXPRESS_LABEL).is_displayed()

    def get_complete_header(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self) -> str:
        return self.get_text(self.COMPLETE_TEXT)
