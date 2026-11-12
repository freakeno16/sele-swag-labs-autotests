from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.checkout_form_pages.base_checkout_page import BaseCheckoutPage


class CheckoutPageStepTwo(BaseCheckoutPage):
    FINISH_BUTTON = (By.ID, 'finish')
    TOTAL_SUM_LABEL = (By.CSS_SELECTOR, '[data-test="total-label"]')
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    TAX_LABEL = (By.CSS_SELECTOR, '[data-test="tax-label"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.endpoint = 'checkout-step-two.html'

    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)

    def get_total_sum(self):
        return self.get_formatted_price(self.TOTAL_SUM_LABEL)

    def get_first_item_price(self):
        return self.get_formatted_price(self.INVENTORY_ITEM_PRICE)

    def get_tax(self):
        return self.get_formatted_price(self.TAX_LABEL)

    def get_expected_total_sum(self):
        return round(self.get_first_item_price() + self.get_tax(), 2)
