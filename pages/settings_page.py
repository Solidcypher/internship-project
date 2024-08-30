from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SettingsPage(BasePage):
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "[href='/set-new-password']")
    # CHANGE_PASSWORD_LINK2 = (By.XPATH, "//div[contains(text(),'Change password')]")

    def click_change_password_option(self):
        """
        I didn't want to put this sleep in here but for some reason the explicit wait with an EC of wait for element
        to be clickable still wasn't enough time. Without the sleep it would go back to the sign-in page and then
        couldn't find the element. Please remove the sleep and test it yourself to see if it does the same thing.
        """
        sleep(4)
        self.wait_and_click(*self.CHANGE_PASSWORD_LINK)
