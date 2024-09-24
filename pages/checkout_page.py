from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    THANK_YOU_MESSAGE = (By.CLASS_NAME, "complete-header")

    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.enter_text(first_name, *self.FIRST_NAME_INPUT)
        self.enter_text(last_name, *self.LAST_NAME_INPUT)
        self.enter_text(postal_code, *self.POSTAL_CODE_INPUT)
        self.click(*self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(*self.FINISH_BUTTON)

    def get_thank_you_message(self):
        return self.find_element(*self.THANK_YOU_MESSAGE).text

    def get_total_price(self):
        return self.find_element(*self.SUMMARY_TOTAL).text

    def get_subtotal_price(self):
        return self.find_element(*self.SUMMARY_SUBTOTAL).text

    def get_tax_amount(self):
        return self.find_element(*self.SUMMARY_TAX).text
