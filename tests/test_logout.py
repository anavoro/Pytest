from playwright.sync_api import Page
from pages.home_page import HomePage

def test_user_logout(logged_in_user: Page): 
    page = logged_in_user
    home_page = HomePage(page)

    assert home_page.is_logout_button_visible()

    home_page.click_logout_account()

    assert home_page.is_signup_login_button_visible()