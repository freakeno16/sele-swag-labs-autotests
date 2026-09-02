import pytest
from pages.inventory_page import InventoryPage
from pages.login.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def inventory_page(driver):
    inventory_page = InventoryPage(driver)
    return inventory_page

