from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import math


class OffPlanOldPage(BasePage):
    TOTAL_PROPERTIES = (By.CSS_SELECTOR, "[wized='totalPropertyCounter']")
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
    PREV_PAGE_BTN = (By.CSS_SELECTOR, "[wized='previousPageProperties']")

    def click_through_off_plan_pages(self):
        sleep(2)
        total_properties = self.find_element(*self.TOTAL_PROPERTIES).text
        total_pages = int(total_properties) / 24
        total_pages_rounded = math.ceil(total_pages)
        for i in range(1, int(total_pages_rounded) + 1):
            sleep(1)
            self.driver.execute_script(f"window.scrollBy(0, 5000)", "")
            self.wait_and_click(*self.NEXT_PAGE_BTN)

    def click_back_through_off_plan_pages(self):
        sleep(2)
        total_properties = self.find_element(*self.TOTAL_PROPERTIES).text
        total_pages = int(total_properties) / 24
        total_pages_rounded = math.ceil(total_pages)
        for i in range(1, int(total_pages_rounded) + 1):
            sleep(1)
            self.driver.execute_script(f"window.scrollBy(0, 5000)", "")
            self.wait_and_click(*self.PREV_PAGE_BTN)

    def verify_old_off_plan_page_opens(self):
        self.verify_partial_url('/off-plan')
