import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage
from pages.signup_account import SignupInfoPage
from pages.account_pages import AccountCreatedPage, AccountDeletedPage
from faker import Faker

def test_register_user(page: Page):
    fake = Faker()
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_info_page = SignupInfoPage(page)
    account_created_page = AccountCreatedPage(page)
    account_deleted_page = AccountDeletedPage(page)
    

    home_page.navigate('http://automationexercise.com')
    
    assert home_page.is_home_page_visible()
    assert 'automationexercise.com' in home_page.get_url()
    assert home_page.get_title() == 'Automation Exercise'
    
    home_page.open_login_menu()
    
    try:
        page.wait_for_url('**/automationexercise.com/login', timeout=10000)
    except:
        page.wait_for_url('**/login', timeout=10000)
    
    assert 'login' in page.url
    
    assert page.locator('h2:has-text("New User Signup!")').is_visible()
    
    signup_name = fake.name()
    signup_email = fake.email()
    login_page.enter_signup_name(signup_name)
    login_page.enter_signup_email(signup_email)
    
    with page.expect_navigation(timeout=10000, url="**/signup"):
        login_page.click_signup_button()
    
    assert signup_info_page.verify_enter_account_info_is_visible()
    
    signup_info_page.select_gender('Mr')
    signup_info_page.enter_name(signup_name)
    signup_info_page.enter_password(fake.password())
    signup_info_page.select_date('10')
    signup_info_page.select_month('5')
    signup_info_page.select_year('1990')
    signup_info_page.subscribe_newsletter()
    signup_info_page.receive_special_offers()
    signup_info_page.enter_first_name(fake.first_name())
    signup_info_page.enter_last_name(fake.last_name())
    signup_info_page.enter_address1(fake.street_address())
    signup_info_page.select_country('Canada')
    signup_info_page.enter_state(fake.state())
    signup_info_page.enter_city(fake.city())
    signup_info_page.enter_zipcode(fake.zipcode())
    signup_info_page.enter_mobile_number(fake.phone_number())
    
    signup_info_page.click_create_account_button()
    
    assert account_created_page.is_account_created_visible(), "'ACCOUNT CREATED!' message is not visible"

    account_created_page.click_continue() 
    
    assert home_page.is_logged_in_as_visible(signup_name), f"'Logged in as {signup_name}' is not visible"

    home_page.click_delete_account()
    
    assert account_deleted_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"
    
    account_deleted_page.click_continue()
    assert home_page.is_home_page_visible()