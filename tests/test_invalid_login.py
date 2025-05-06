from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage
from faker import Faker

def test_login_with_invalid_credentials(page: Page):
    fake = Faker()
    home_page = HomePage(page)
    login_page = LoginPage(page)
    
    # Navigate to login page
    home_page.navigate('http://automationexercise.com')
    home_page.open_login_menu()
    page.wait_for_url('**/login', timeout=10000)
    
    # Generate random credentials (which should be invalid)
    email = fake.email()
    password = fake.password()
    
    # Attempt login with combined method
    login_page.login(email, password)
    
    # Verify error message appears
    assert login_page.is_visible(login_page.login_error_message)
    expected_error = 'Your email or password is incorrect!'
    assert login_page.get_error_message_text() == expected_error