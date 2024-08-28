from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    PAGE_EXPECTED_TXT = 'Change password'
    EXPECTED_URL = 'https://soft.reelly.io/set-new-password'
    CHANGE_PASSWORD_TXT = (By.XPATH, "//div[contains(text(),'Change password')]")
    NEW_PASSWORD_FIELD = (By.ID, 'Enter-new-password')
    REPEAT_PASSWORD_FIELD = (By.ID, 'Repeat-password')
    TEST_PASSWORD = 'Test'
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "a[wized='changePasswordButton']")

    def input_test_password(self):
        self.input_text(self.TEST_PASSWORD, *self.NEW_PASSWORD_FIELD)
        self.input_text(self.TEST_PASSWORD, *self.REPEAT_PASSWORD_FIELD)

    def verify_change_password_page_appears(self):
        self.verify_text(self.PAGE_EXPECTED_TXT, *self.CHANGE_PASSWORD_TXT)
        self.verify_url(self.EXPECTED_URL)

    def verify_change_password_button(self):
        assert self.find_element(*self.CHANGE_PASSWORD_BTN), f"{self.CHANGE_PASSWORD_BTN} not found"



