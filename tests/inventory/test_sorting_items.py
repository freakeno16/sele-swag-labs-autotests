from data.inventory.sort_types import SORT_TYPES


def test_sort_items_by_price_from_low_to_high(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["price_low_to_high"])
    actual_prices = auth_inventory_page.get_items_sorted_by(SORT_TYPES["price_low_to_high"])

    assert actual_prices == sorted(actual_prices)

def test_sort_items_by_price_from_high_to_low(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["price_high_to_low"])
    actual_prices = auth_inventory_page.get_items_sorted_by(SORT_TYPES["price_high_to_low"])

    assert actual_prices == sorted(actual_prices, reverse=True)


def test_sort_items_by_name_from_a_to_z(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["name_a_to_z"])
    actual_names = auth_inventory_page.get_items_sorted_by(SORT_TYPES["name_a_to_z"])

    assert actual_names == sorted(actual_names)

def test_sort_items_by_name_from_z_to_a(auth_inventory_page):
    auth_inventory_page.sort_items_by(SORT_TYPES["name_z_to_a"])
    actual_names = auth_inventory_page.get_items_sorted_by(SORT_TYPES["name_z_to_a"])

    assert actual_names == sorted(actual_names, reverse=True)
