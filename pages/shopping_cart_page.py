from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = 'cart.html'

    def click_continue_shopping_button(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def get_all_item_names_in_cart(self):
        return [name.text for name in self.find_all(self.CART_ITEM_NAME)]
