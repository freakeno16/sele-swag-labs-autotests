import pytest
from selenium import webdriver
from pages.inventory_page import InventoryPage
from tests.login.conftest import valid_creds


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

@pytest.fixture
def auth_inventory_page(driver, valid_creds, login_page):
    login_page.open()
    login_page.login(valid_creds["standard_user_username"], valid_creds["password"])

    inventory_page = InventoryPage(driver)

    yield inventory_page
