from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SettingsPage(BasePage):
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "[href='/set-new-password']")
    # CHANGE_PASSWORD_LINK2 = (By.XPATH, "//div[contains(text(),'Change password')]")
    SETTINGS_CELLS = (By.XPATH, "//a[@class='page-setting-block w-inline-block']")
    CONNECT_COMPANY_BTN = (By.CSS_SELECTOR, "[href='/book-presentation']")

    def click_change_password_option(self):
        """
        I didn't want to put this sleep in here but for some reason the explicit wait with an EC of wait for element
        to be clickable still wasn't enough time. Without the sleep it would go back to the sign-in page and then
        couldn't find the element. Please remove the sleep and test it yourself to see if it does the same thing.
        """
        self.scroll_down(500)
        sleep(3)
        self.wait_and_click(*self.CHANGE_PASSWORD_LINK)

    def verify_settings_options(self, number):
        options = self.find_elements(*self.SETTINGS_CELLS)

        assert len(options) == int(number), f"Expected {number} options cells but got {len(options)}"

    def verify_connect_the_company_button(self):
        connect_btns = self.find_elements(*self.CONNECT_COMPANY_BTN)

        assert connect_btns[1], f"Expected Connect Company Button but got {connect_btns[1]}"
