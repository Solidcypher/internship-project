from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from time import sleep


class SecondaryPage(BasePage):
    NEXT_PG_BTN = (By.CSS_SELECTOR, "[wized='nextPageMLS']")
    FILTER_BTN = (By.CLASS_NAME, "filter-button")
    FROM_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    TO_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    LISTING_CARDS = (By.CSS_SELECTOR, "[wized='listingCardMLS']")
    UNIT_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceMLS']")
    CURRENT_PG = (By.CSS_SELECTOR, "[wized='currentPageProperties']")
    TOTAL_PG = (By.CSS_SELECTOR, "[wized='totalPageProperties']")

    def click_through_all_pages(self, number):
        for i in range(1, int(number) + 1):
            self.driver.execute_script(f"window.scrollBy(0, 5000)", "")
            sleep(3)
            if i == int(number):
                break
            self.wait_and_click(*self.NEXT_PG_BTN)

    def click_filter_button(self):
        sleep(5)
        self.wait_and_click(*self.FILTER_BTN)

    def input_from_price(self, number):
        self.input_text(number, *self.FROM_PRICE)

    def input_to_price(self, number):
        self.input_text(number, *self.TO_PRICE)

    def click_apply_filter_btn(self):
        self.wait_and_click(*self.APPLY_FILTER_BTN)
        sleep(5)

    def verify_secondary_pages_opens(self):
        self.verify_partial_url('/secondary-listings')

    def verify_card_price_range(self, page_number, number1, number2):
        price_element = self.find_element(*self.UNIT_PRICE)
        raw_price = price_element.text.strip().replace('\u00A0', ' ')
        stripped_price = int(raw_price.replace("AED", " ").replace(",", "").strip())
        for cards in self.LISTING_CARDS:
            assert int(number1) <= stripped_price <= int(number2), (
                f"Price {stripped_price} in not within the expected range (1,200,000 - 2,000,000)"
            )
            #self.click_through_all_pages(page_number)
