from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[contains(text(),'Settings')]")

    def click_settings(self):
        self.wait_and_click(*self.SETTINGS_LINK)


