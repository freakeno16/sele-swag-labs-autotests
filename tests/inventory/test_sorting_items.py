import time
from test_data.inventory.sort_types import SORT_TYPES

def test_sort_items_by_price_from_low_to_high(
    auth_inventory_page,
    # valid_creds,
    # login_page,
    # inventory_page
):
    # login_page.open()
    # login_page.login(valid_creds["standard_user_username"], valid_creds["password"])

    auth_inventory_page.sort_items_by(SORT_TYPES["price_low_to_high"])
    # time.sleep(5)