from playwright.sync_api import Page
from pages.base_page import BasePage  

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_login_button = 'a[href="/login"]'
        self.logout_button = 'a[href="/logout"]'
        self.home_page_title = 'Automation Exercise'
        self.logged_in_as = "a:has-text('Logged in as')"
        self.delete_account_button = "a:has-text('Delete Account')"
        self.contact_us_link = "a[href='/contact_us']"
        self.test_cases_link = "a:has-text('Test Cases')"
        self.products_button = 'a[href="/products"]'
        self.subscription_text = 'h2:has-text("Subscription")'
        self.subscription_email_input = '#susbscribe_email'
        self.subscription_button = '#subscribe'
        self.subscription_success_message = '.alert-success.alert'


    def open_login_menu(self):
        self.click(self.signup_login_button)

    def is_home_page_visible(self):
        return self.get_title() == self.home_page_title

    def is_logged_in_as_visible(self, username=None):
        if username:
            selector = f"a:has-text('Logged in as {username}')"
            return self.is_visible(selector)
        return self.is_visible(self.logged_in_as)

    def get_logged_in_username(self) -> str:
        return self.get_text(self.logged_in_as)

    def click_delete_account(self):
        self.click(self.delete_account_button)

    def click_logout_account(self): 
        self.click(self.logout_button) 

    def is_logout_button_visible(self, timeout: int = 5000) -> bool:
        return self.is_visible(self.logout_button, timeout)

    def is_signup_login_button_visible(self, timeout: int = 5000) -> bool:
        return self.is_visible(self.signup_login_button, timeout)

    def navigate_to_contact_us(self):
        self.click(self.contact_us_link)
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_test_cases(self):
        self.click(self.test_cases_link)
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_products(self):
        self.click(self.products_button)
        self.page.wait_for_load_state("domcontentloaded")

    def is_subscription_text_visible(self):
        return self.page.is_visible(self.subscription_text)

    def subscribe_with_email(self, email: str):
        self.page.fill(self.subscription_email_input, email)
        self.page.click(self.subscription_button)

    def is_subscription_success_visible(self):
        return self.page.is_visible(self.subscription_success_message)
