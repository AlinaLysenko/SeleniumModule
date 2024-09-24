from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_HEADER = (By.CLASS_NAME, "title")
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    OPEN_CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    class Product:
        def __init__(self, item):
            self.name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            self.price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            self.add_button = item.find_element(By.CLASS_NAME, "btn_inventory")

        def get_price_as_float(self):
            return float(self.price.replace('$', ''))

    def get_all_products(self):
        product_elements = self.find_elements(*self.PRODUCT_LIST)
        products = []

        for product_element in product_elements:
            product = self.Product(product_element)
            products.append(product)
        self.products = products
        return products

    def add_to_cart(self, products):
        if isinstance(products, list):
            for product in products:
                product.add_button.click()
        else:
            products.add_button.click()

    def calculate_total_price(self, products):
        total_price = sum(product.get_price_as_float() for product in products)
        return total_price

    def get_inventory_title(self):
        return self.find_element(*self.INVENTORY_HEADER).text

    def is_product_list_displayed(self):
        return len(self.find_elements(*self.PRODUCT_LIST)) > 0

    def open_cart(self):
        self.click(*self.OPEN_CART_BUTTON)
