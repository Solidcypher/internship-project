from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from pages.secondary_page import SecondaryPage
from pages.off_plan_old_page import OffPlanOldPage
from pages.change_password_page import ChangePasswordPage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.settings_page = SettingsPage(driver)
        self.change_password_page = ChangePasswordPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_old_page = OffPlanOldPage(driver)
