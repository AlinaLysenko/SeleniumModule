from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def get_cart_items(self):
        return self.find_elements(*self.CART_ITEMS)

    def click_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)
