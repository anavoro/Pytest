from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Top navigation
        self.signup_login_button: Locator = page.locator('a[href="/login"]')
        self.logout_button: Locator = page.locator('a[href="/logout"]')
        self.logged_in_as_text = page.locator("a", has_text="Logged in as")
        self.delete_account_button: Locator = page.locator("a:has-text('Delete Account')")

        # Navigation links
        self.contact_us_link: Locator = page.locator("a[href='/contact_us']")
        self.test_cases_link: Locator = page.get_by_role("link", name="Test Cases", exact=True)
        self.products_button: Locator = page.locator('a[href="/products"]')

        # Subscription section
        self.subscription_text: Locator = page.locator('h2:has-text("Subscription")')
        self.subscription_email_input: Locator = page.locator('#susbscribe_email')
        self.subscription_button: Locator = page.locator('#subscribe')
        self.subscription_success_message: Locator = page.locator('.alert-success.alert')

        # Page metadata
        self.home_page_title: str = 'Automation Exercise'

    # ---------- Navigation ----------
    def open_login_menu(self):
        """Clicks the 'Signup / Login' button."""
        self.signup_login_button.wait_for(state="visible", timeout=5000)
        self.signup_login_button.click()

    def navigate_to_contact_us(self):
        self.contact_us_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_test_cases(self):
        self.test_cases_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_products(self):
        self.products_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ---------- Page Status ----------
    def wait_for_home_page_to_load(self, timeout: int = 10000):
        self.page.wait_for_load_state("load", timeout=timeout)

    def is_home_page_visible(self, timeout: int = 10000) -> bool:
        """Check if the current page title matches the expected home page title."""
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
            return self.get_title() == self.home_page_title
        except Exception:
            return False

    # ---------- Authentication ----------
    def is_logged_in_as_visible(self, username: str = None) -> bool:
        if username:
           return self.page.locator("a", has_text=f"Logged in as {username}").is_visible()
        return self.logged_in_as_text.is_visible()

    def get_logged_in_username(self) -> str:
        text = self.logged_in_as_text.inner_text()
        return text.replace("Logged in as", "").strip()

    def click_delete_account(self):
        self.delete_account_button.wait_for(state="visible", timeout=5000)
        self.delete_account_button.click()

    def click_logout_account(self):
        self.logout_button.wait_for(state="visible", timeout=5000)
        self.logout_button.click()

    def is_logout_button_visible(self, timeout: int = 5000) -> bool:
        """Check if the logout button is visible."""
        try:
            self.logout_button.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def is_signup_login_button_visible(self, timeout: int = 5000) -> bool:
        """Check if the signup/login button is visible."""
        try:
            self.signup_login_button.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    # ---------- Subscription ----------
    def is_subscription_text_visible(self, timeout: int = 5000) -> bool:
        """Check if the subscription text is visible."""
        try:
            self.subscription_text.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def subscribe_with_email(self, email: str):
        """Fill the subscription email input and click subscribe."""
        self.subscription_email_input.fill(email)
        self.subscription_button.click()

    def is_subscription_success_visible(self, timeout: int = 5000) -> bool:
        """Check if the subscription success message is visible."""
        try:
            self.subscription_success_message.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False
