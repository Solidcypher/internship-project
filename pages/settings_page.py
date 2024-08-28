from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SettingsPage(BasePage):
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "[href='/set-new-password']")
    # CHANGE_PASSWORD_LINK2 = (By.XPATH, "//div[contains(text(),'Change password')]")

    def click_change_password_option(self):
        self.wait_and_click(*self.CHANGE_PASSWORD_LINK)
