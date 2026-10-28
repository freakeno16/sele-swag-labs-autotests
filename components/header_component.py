from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class HeaderComponent(BaseComponent):
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def click_cart_button(self):
        self.page.click(self.CART_BUTTON)

    def get_cart_badge_number(self):
        return int(self.page.get_text(self.CART_BADGE))