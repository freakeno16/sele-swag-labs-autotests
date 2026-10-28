import pytest
from pages.inventory_page import InventoryPage
from pages.login.login_page import LoginPage
from pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def inventory_page(driver):
    inventory_page = InventoryPage(driver)
    return inventory_page

@pytest.fixture
def shopping_cart_page(driver):
    shopping_cart_page = ShoppingCartPage(driver)
    return shopping_cart_page