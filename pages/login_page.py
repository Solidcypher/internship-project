from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://soft.reelly.io/sign-in'
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    EMAIL = 'marcopolo.skylight490@passin-box.com'
    PASSWORD = '<PASSWORD>'
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open_login_page(self):
        self.open_url(self.URL)

    def input_email(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)

    def input_password(self):
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_login_button(self):
        self.wait_and_click(*self.LOGIN_BUTTON)