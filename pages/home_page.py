from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class HomePage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[contains(text(),'Settings')]")
    MAIN_MENU_BTN = (By.CSS_SELECTOR, ".circle-gradient")
    USER_PROFILE_BTN = (By.CSS_SELECTOR, ".menu-photo_avatar")
    SECONDARY_BTN = (By.CSS_SELECTOR, "[href='/secondary-listings']")
    OFF_PLAN_OLD_BTN = (By.CLASS_NAME, "menu-old")
    OFF_PLAN_NEW_BTN = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")

    def click_settings(self):
        self.wait_and_click(*self.SETTINGS_LINK)

    def click_main_menu(self):
        # I only needed this sleep for when I did the mobile testing on browserstack.
        # sleep(4)
        self.wait_and_click(*self.MAIN_MENU_BTN)

    def click_off_plan_old(self):
        self.wait_and_click(*self.OFF_PLAN_OLD_BTN)

    def click_secondary_listings(self):
        self.wait_and_click(*self.SECONDARY_BTN)

    def click_user_profile_image(self):
        # I only needed this sleep for when I did the mobile testing on browserstack.
        # sleep(4)
        self.wait_and_click(*self.USER_PROFILE_BTN)
