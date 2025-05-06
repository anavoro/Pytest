from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Login selectors
        self.login_email_field = 'input[data-qa="login-email"]'
        self.login_password_field = 'input[data-qa="login-password"]'
        self.login_button = 'button[data-qa="login-button"]'
        self.login_error_message = 'p:has-text("Your email or password is incorrect!")'
        self.error_message = '#login_error'
        
        # Signup selectors
        self.signup_name_field = 'input[data-qa="signup-name"]'
        self.signup_email_field = 'input[data-qa="signup-email"]'
        self.signup_button = 'button[data-qa="signup-button"]'
        self.new_user_signup_heading = 'h2:has-text("New User Signup!")'
        
        self.logout_button = 'a[href="/logout"]'

    # login method
    def login(self, email: str, password: str):
        """Login with the given credentials"""
        self.fill(self.login_email_field, email)
        self.fill(self.login_password_field, password)
        self.click(self.login_button)
    
    # Individual login actions 
    def enter_login_email(self, email: str):
        self.fill(self.login_email_field, email)
        
    def enter_login_password(self, password: str):
        self.fill(self.login_password_field, password)
        
    def click_login_button(self):
        self.click(self.login_button)
    
    # Signup methods  
    def signup(self, name: str, email: str):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup_button()
    
    def enter_signup_name(self, name: str):
        self.fill(self.signup_name_field, name)
        
    def enter_signup_email(self, email: str):
        self.fill(self.signup_email_field, email)
        
    def click_signup_button(self):
        self.click(self.signup_button)
    
    # Validation methods
    def verify_new_user_signup_visible(self):
        return self.is_visible(self.new_user_signup_heading)
    
    def get_error_message_text(self):
        return self.get_text(self.login_error_message)
    
    def is_logged_in(self):
        """Check if user is logged in by verifying logout button is visible"""
        return self.is_visible(self.logout_button)