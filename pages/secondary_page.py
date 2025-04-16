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
    CARD_UNIT_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceMLS']")
    BUY_LISTING_TYPE = (By.CSS_SELECTOR, "[wized='ListingTypeBuy']")
    WANT_BUY_TAG = (By.CSS_SELECTOR, "[wized='saleTagMLS']")
    CURRENT_PG = (By.CSS_SELECTOR, "[wized='currentPageProperties']")
    TOTAL_PG = (By.CSS_SELECTOR, "[wized='totalPageProperties']")

    def click_through_all_secondary_pages(self):
        total_page = int(self.driver.find_element(*self.TOTAL_PG).text)
        for i in range(1, int(total_page) + 1):
            self.driver.execute_script(f"window.scrollBy(0, 5000)", "")
            sleep(1)
            if i == int(total_page):
                break
            self.wait_and_click(*self.NEXT_PG_BTN)

    def click_filter_button(self):
        sleep(3)
        self.wait_and_click(*self.FILTER_BTN)

    def click_buy_listing_type(self):
        self.wait_and_click(*self.BUY_LISTING_TYPE)

    def input_from_price(self, number):
        self.input_text(number, *self.FROM_PRICE)

    def input_to_price(self, number):
        self.input_text(number, *self.TO_PRICE)

    def click_apply_filter_btn(self):
        self.wait_and_click(*self.APPLY_FILTER_BTN)
        sleep(5)

    def verify_secondary_pages_opens(self):
        self.verify_partial_url('/secondary-listings')

    def verify_card_want_to_buy_tag(self):
        for cards in self.LISTING_CARDS:
            self.verify_text("Want to buy", *self.WANT_BUY_TAG)
            self.click_through_all_secondary_pages()

    def verify_card_price_range(self, number1, number2):
        price_element = self.find_element(*self.CARD_UNIT_PRICE)
        raw_price = price_element.text.strip().replace('\u00A0', ' ')
        stripped_price = int(raw_price.replace("AED", " ").replace(",", "").strip())
        for cards in self.LISTING_CARDS:
            assert int(number1) <= stripped_price <= int(number2), (
                f"Price {stripped_price} in not within the expected range (1,200,000 - 2,000,000)"
            )
            self.click_through_all_secondary_pages()
