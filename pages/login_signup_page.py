from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_email_field = 'input[data-qa="login-email"]'
        self.login_password_field = 'input[data-qa="login-password"]'
        self.login_button = 'button[data-qa="login-button"]'
        self.signup_name_field = 'input[data-qa="signup-name"]'
        self.signup_email_field = 'input[data-qa="signup-email"]'
        self.signup_button = 'button[data-qa="signup-button"]'
        self.logout_button = 'a[href="/logout"]'
        self.error_message = '#login_error'    

    new_user_signup_heading = 'h2:has-text("New User Signup!")'
    # Login related methods
    def enter_login_email(self, email: str):
        self.fill(self.login_email_field, email)

    def enter_login_password(self, password: str):
        self.fill(self.login_password, password)

    def click_login_button(self):
        self.click(self.login_button)

    # Signup related methods 
    def enter_signup_name(self, name: str):
        self.fill(self.signup_name_field, name)

    def enter_signup_email(self, email: str):
        self.fill(self.signup_email_field, email)

    def click_signup_button(self):
        self.click(self.signup_button)
        
    def verify_new_user_signup_visible(self):
        return self.is_visible(self.new_user_signup_heading)
 