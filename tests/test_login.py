import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize("username, password, expected_error", [
    ("invalid_user", "invalid_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required")
])
def test_invalid_login(setup, username, password, expected_error):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(username, password)
    error_message = login_page.get_error_message()
    assert error_message == expected_error, f"Expected error message: {expected_error}, but got: {error_message}"


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.get_inventory_title() == "Products"
    assert inventory_page.is_product_list_displayed() == True
