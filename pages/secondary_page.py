from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SecondaryPage(BasePage):
    NEXT_PG_BTN = (By.CSS_SELECTOR, "[wized='nextPageMLS']")

    def click_through_all_pages(self, number):
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        sleep(3)
        self.wait_and_click(*self.NEXT_PG_BTN)

    def verify_secondary_pages_opens(self):
        self.verify_partial_url('/secondary-listings')
