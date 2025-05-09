from playwright.sync_api import Page
from pages.base_page import BasePage  

class AccountCreatedPage(BasePage):  
    def __init__(self, page: Page):
        super().__init__(page)
        self.account_created_message = "[data-qa='account-created']"
        self.continue_button = "[data-qa='continue-button']"
  
    def is_account_created_visible(self, timeout: int = 5000) -> bool:
        return self.is_visible(self.account_created_message, timeout)
    
    def click_continue(self):
        self.click(self.continue_button)

class AccountDeletedPage(BasePage): 
    def __init__(self, page: Page):
        super().__init__(page)
        self.account_deleted_message = "[data-qa='account-deleted']"
        self.continue_button = "[data-qa='continue-button']"
    
    def is_account_deleted_visible(self, timeout: int = 5000) -> bool:
        return self.is_visible(self.account_deleted_message, timeout)
    
    def click_continue(self):
        self.click(self.continue_button)
