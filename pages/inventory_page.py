from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from test_data.inventory.sort_types import SORT_TYPES


class InventoryPage(BasePage):
    INVENTORY = (By.CLASS_NAME, "inventory_container")
    SORT_SELECT_FIELD = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = "inventory.html"

    def check_inventory_is_visible(self):
        assert self.find(self.INVENTORY).is_displayed()

    def formate_prices(self):
        inventory_prices = self.driver.find_elements(*self.INVENTORY_PRICE)
        for price in inventory_prices:
            print(price.text)
        formatted_prices = [float(price.text.replace('$', '')) for price in inventory_prices]
        print(formatted_prices)
        return formatted_prices

    def sort_items_by(self, sort_type):
        select_field = Select(self.find(self.SORT_SELECT_FIELD))
        select_field.select_by_value(sort_type)
