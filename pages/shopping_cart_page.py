from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_form_pages.step_one_checkout_page import CheckoutPageStepOne


class ShoppingCartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    CART_ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.endpoint = 'cart.html'

    def click_continue_shopping_button(self) -> None:
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_checkout_button(self) -> CheckoutPageStepOne:
        self.click(self.CHECKOUT_BUTTON)

        return CheckoutPageStepOne(self.driver)

    def get_all_item_names_in_cart(self) -> list[str]:
        return [name.text for name in self.find_all(self.CART_ITEM_NAME)]

    def get_all_item_prices_in_cart(self):
        print(self.formate_prices())
