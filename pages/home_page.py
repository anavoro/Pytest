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

    def open_login_menu(self):
        self.click(self.signup_login_button)

    def is_home_page_visible(self):
        return self.page.title() == self.home_page_title

    def is_logged_in_as_visible(self, username=None):
        """Verify that 'Logged in as username' is visible"""
        if username:
            selector = f"a:has-text('Logged in as {username}')"
            return self.page.is_visible(selector)
        return self.page.is_visible(self.logged_in_as)

    def get_logged_in_username(self) -> str:
        """Get the displayed username after login"""
        return self.page.inner_text(self.logged_in_as)

    def click_delete_account(self):
        """Click the 'Delete Account' button"""
        self.click(self.delete_account_button)

    def click_logout_account(self): 
        self.click(self.logout_button) 

    def is_logout_button_visible(self, timeout: int = 5000) -> bool:
        """Checks if the logout button is visible."""
        try:
            self.page.wait_for_selector(self.logout_button, state='visible', timeout=timeout)
            return True
        except:
            return 
        
    def is_signup_login_button_visible(self, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(self.signup_login_button, state='visible', timeout=timeout)
            return True
        except:
            return