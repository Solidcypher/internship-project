from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class HomePage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[contains(text(),'Settings')]")
    MAIN_MENU_BTN = (By.CSS_SELECTOR, ".circle-gradient")
    USER_PROFILE_BTN = (By.CSS_SELECTOR, ".menu-photo_avatar")

    def click_settings(self):
        self.wait_and_click(*self.SETTINGS_LINK)

    def click_main_menu(self):
        # I only needed this sleep for when I did the mobile testing on browserstack.
        # sleep(4)
        self.wait_and_click(*self.MAIN_MENU_BTN)

    def click_user_profile_image(self):
        # I only needed this sleep for when I did the mobile testing on browserstack.
        # sleep(4)
        self.wait_and_click(*self.USER_PROFILE_BTN)


