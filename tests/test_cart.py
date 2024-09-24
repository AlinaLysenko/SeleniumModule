import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def login_and_navigate_to_inventory(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    return driver


def test_add_item_to_cart(login_and_navigate_to_inventory):
    driver = login_and_navigate_to_inventory
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    products = inventory_page.get_all_products()
    test_products = [products[i] for i in [2, 5]]
    inventory_page.add_to_cart(test_products)
    expected_sum = inventory_page.calculate_total_price(test_products)
    expected_tax = round(expected_sum * 0.08, 2)
    expected_total = expected_sum + expected_tax

    inventory_page.open_cart()

    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in the cart."

    assert len(cart_items) == 2, f"Expected 2 items in the cart, but got {len(cart_items)}"
    cart_page.click_checkout()

    checkout_page.fill_checkout_info("John", "Doe", "12345")

    assert f"Total: ${expected_total}" in checkout_page.get_total_price(), "Total price is incorrect"
    assert f"${expected_sum}" in checkout_page.get_subtotal_price(), "Subtotal is incorrect"
    assert f"${expected_tax}" in checkout_page.get_tax_amount(), "Tax amount is incorrect"

    # Завершаем чекаут
    checkout_page.finish_checkout()

    # Проверяем сообщение после завершения чекаута
    thank_you_message = checkout_page.get_thank_you_message()
    assert thank_you_message == "Thank you for your order!", "Checkout was not successful"
