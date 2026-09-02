from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY = (By.CLASS_NAME, "inventory_container")

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = "inventory.html"

    def check_inventory_is_visible(self):
        assert self.find(self.INVENTORY).is_displayed()

