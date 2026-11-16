from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCartPage


class BaseCheckoutPage(BasePage):
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_cancel_button(self) -> ShoppingCartPage:
        self.click(self.CANCEL_BUTTON)

        return ShoppingCartPage(self.driver)

    def get_formatted_price(self, locator) -> float:
        text = self.get_text(locator)
        formatted = text.replace("Total: ", "").replace("Tax: ", "").replace("$", "").replace(",", "")

        return float(formatted)