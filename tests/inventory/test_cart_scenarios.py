import time


def test_add_item_to_cart_button(auth_inventory_page):
    auth_inventory_page.add_random_item_to_cart()
    time.sleep(2)