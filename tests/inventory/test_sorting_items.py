from test_data.inventory.sort_types import SORT_TYPES


def test_sort_items_by_price_from_low_to_high(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["price_low_to_high"])
    auth_inventory_page.check_items_sorting_by(SORT_TYPES["price_low_to_high"])


def test_sort_items_by_price_from_high_to_low(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["price_high_to_low"])
    auth_inventory_page.check_items_sorting_by(SORT_TYPES["price_high_to_low"])


def test_sort_items_by_name_from_a_to_z(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["name_a_to_z"])
    auth_inventory_page.check_items_sorting_by(SORT_TYPES["name_a_to_z"])


def test_sort_items_by_name_from_z_to_a(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["name_z_to_a"])
    auth_inventory_page.check_items_sorting_by(SORT_TYPES["name_z_to_a"])
