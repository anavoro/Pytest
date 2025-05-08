from playwright.sync_api import Page

class AccountCreatedPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_created_message = "[data-qa='account-created']"
        self.continue_button = "[data-qa='continue-button']"
    
    def is_account_created_visible(self):
        """Verify that 'ACCOUNT CREATED!' message is visible"""
        return self.page.is_visible(self.account_created_message)
    
    def click_continue(self):
        """Click the 'Continue' button"""
        self.page.click(self.continue_button)

class AccountDeletedPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_deleted_message = "[data-qa='account-deleted']"
        self.continue_button = "[data-qa='continue-button']"
    
    def is_account_deleted_visible(self, timeout: int = 5000) -> bool:
        """Wait for and verify 'ACCOUNT DELETED!' message is visible"""
        try:
            self.page.wait_for_selector(self.account_deleted_message, state="visible", timeout=timeout)
            return True
        except:
            return False
    
    def click_continue(self):
        """Click the 'Continue' button"""
        self.page.click(self.continue_button)