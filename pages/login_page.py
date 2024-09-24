from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.enter_text(username, *self.USERNAME_INPUT)
        self.enter_text(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text
