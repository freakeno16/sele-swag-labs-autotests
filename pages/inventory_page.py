from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from test_data.inventory.sort_types import SORT_TYPES


class InventoryPage(BasePage):

    INVENTORY = (By.CSS_SELECTOR, "[data-test='inventory-list']")
    SORT_SELECT_FIELD = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    INVENTORY_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = "inventory.html"

    def check_inventory_is_visible(self):
        assert self.find(self.INVENTORY).is_displayed()

    def formate_prices(self):
        inventory_prices = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        formatted_prices = [float(price.text.replace('$', '')) for price in inventory_prices]

        return formatted_prices

    def sort_items_by(self, sort_type):
        select_field = Select(self.find(self.SORT_SELECT_FIELD))
        select_field.select_by_value(sort_type)

    def check_items_sorting_by(self, sort_type):
        if sort_type == SORT_TYPES["price_low_to_high"]:
            formatted_prices = self.formate_prices()

            assert sorted(formatted_prices) == formatted_prices

        elif sort_type == SORT_TYPES["price_high_to_low"]:
            formatted_prices = self.formate_prices()

            assert sorted(formatted_prices, reverse=True) == formatted_prices

        elif sort_type == SORT_TYPES["name_a_to_z"]:
            inventory_names_elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
            inventory_names = [name.text for name in inventory_names_elements]

            assert inventory_names == sorted(inventory_names)

        else:
            inventory_names_elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
            inventory_names = [name.text for name in inventory_names_elements]

            assert inventory_names == sorted(inventory_names, reverse=True)

