from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_to_input_text(self, text, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} not visible'
        ).send_keys(text)

    def scroll_down(self, amount):
        self.driver.execute_script(f"window.scrollBy(0, {amount})", "")

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} not visible'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, f'Expected {expected_partial_text} not in actual {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected {expected_url} didn't match {actual_url}"

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f"Expected {expected_partial_url} not in {actual_url}"
