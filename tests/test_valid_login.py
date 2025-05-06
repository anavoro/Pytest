from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage
from utils.signup_fixture import new_user_data
from pages.account_pages import AccountDeletedPage

def test_login_with_valid_credentials(page: Page, new_user_data):
    page_from_fixture, email, password = new_user_data
    
    # Initialize page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_deleted_page = AccountDeletedPage(page)
    
    # Navigate to login page
    home_page.open_login_menu()
    page.wait_for_url('**/login', timeout=10000)
    
    # Use the combined login method instead of individual steps
    login_page.login(email, password)
    
    # Verify login was successful
    assert home_page.is_logout_button_visible()
    
    # Clean up - delete account
    home_page.click_delete_account()
    assert account_deleted_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"
    account_deleted_page.click_continue()
    assert home_page.is_home_page_visible()
