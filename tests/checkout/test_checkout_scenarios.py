from pages.checkout_form_pages.step_one_checkout_page import CheckoutPageStepOne
from pages.checkout_form_pages.step_two_checkout_page import CheckoutPageStepTwo
from pages.shopping_cart_page import ShoppingCartPage
from data import checkout_userdata

def test_checkout_with_empty_cart_has_zero_total(auth_inventory_page):
    auth_inventory_page.header.click_cart_button()

    shopping_cart_page = ShoppingCartPage(auth_inventory_page.driver)
    shopping_cart_page.click_checkout_button()

    checkout_page_step_one = CheckoutPageStepOne(shopping_cart_page.driver)
    checkout_page_step_one.fill_firstname_field(checkout_userdata.first_name)
    checkout_page_step_one.fill_lastname_field(checkout_userdata.last_name)
    checkout_page_step_one.fill_postal_code_field(checkout_userdata.postal_code)
    checkout_page_step_one.click_continue_button()
    checkout_page_step_two = CheckoutPageStepTwo(checkout_page_step_one.driver)

    assert checkout_page_step_two.get_total_sum() == 0.00

def test_single_item_total_is_sum_of_price_and_tax(auth_inventory_page):
    auth_inventory_page.add_random_item_to_cart()
    auth_inventory_page.header.click_cart_button()

    shopping_cart_page = ShoppingCartPage(auth_inventory_page.driver)
    shopping_cart_page.click_checkout_button()

    checkout_page_step_one = CheckoutPageStepOne(shopping_cart_page.driver)
    checkout_page_step_one.fill_firstname_field(checkout_userdata.first_name)
    checkout_page_step_one.fill_lastname_field(checkout_userdata.last_name)
    checkout_page_step_one.fill_postal_code_field(checkout_userdata.postal_code)
    checkout_page_step_one.click_continue_button()
    checkout_page_step_two = CheckoutPageStepTwo(checkout_page_step_one.driver)

    assert checkout_page_step_two.get_total_sum() == checkout_page_step_two.get_expected_total_sum()
