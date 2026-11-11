import os
import pytest
from selenium import webdriver
from pages.inventory_page import InventoryPage
from tests.login.conftest import valid_creds


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()

    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    else:
        chrome_options.add_argument("--start-maximized")

    chrome_options.add_experimental_option(
        "prefs",
        {"profile.password_manager_leak_detection": False},
    )

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()

@pytest.fixture
def auth_inventory_page(driver, valid_creds, login_page):
    login_page.open()
    login_page.login(valid_creds["standard_user_username"], valid_creds["password"])

    inventory_page = InventoryPage(driver)

    yield inventory_page
