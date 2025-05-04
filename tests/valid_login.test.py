import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage

def test_login_with_valid_credentials_sync(page: Page, new_user_data):
    email, password = new_user_data[1], new_user_data[2] # Get email and password from fixture
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open_login_menu()
    page.wait_for_url('**/login', timeout=10000)
    login_page.enter_login_email(email)
    login_page.enter_login_password(password)
    login_page.click_login_button()
    assert home_page.is_logout_button_visible()