import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage


@pytest.fixture(scope="function")
def logged_in_user(page: Page):
    page.goto("http://automationexercise.com")
    home_page = HomePage(page)
    home_page.open_login_menu()
    page.wait_for_url("**/login", timeout=10000)
    login_page = LoginPage(page)
    login_page.login("test-pytest@example.com", "test123")
    assert login_page.is_logged_in(), "Failed to log in"
    return page