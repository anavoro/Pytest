import sys
import os
from pathlib import Path
import pytest
from playwright.sync_api import Page, Playwright
from faker import Faker
import allure
from pages.home_page import HomePage
from pages.login_signup_page import LoginPage
from pages.account_pages import AccountDeletedPage, AccountCreatedPage
from pages.signup_account import SignupInfoPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

fake = Faker()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')

@pytest.fixture(scope="session")
def faker():
    return Faker()

@pytest.fixture(scope="function")
def test_setup(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser_name")
    headless = not request.config.getoption("--headed")

    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=headless)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto("https://automationexercise.com", wait_until="domcontentloaded", timeout=20000)
    yield {
        "page": page,
        "home_page": HomePage(page),
        "login_page": LoginPage(page),
        "account_deleted_page": AccountDeletedPage(page),
        "signup_info_page": SignupInfoPage(page),
        "account_created_page": AccountCreatedPage(page),
        "contact_us_page": ContactUsPage(page),
        "test_cases_page": TestCasesPage(page),
        "products_page": ProductsPage(page),
        "product_details_page": ProductDetailsPage(page),
    }

    browser.close()

@pytest.fixture(scope="function")
def login_page_setup(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://automationexercise.com', wait_until='domcontentloaded', timeout=20000)
    home_page = HomePage(page)
    login_page = LoginPage(page)
    
    home_page.open_login_menu()
    try:
        page.wait_for_url('**/login', timeout=10000)
    except:
        pass 
    
    return {
        "page": page,
        "home_page": home_page,
        "login_page": login_page
    }

@pytest.fixture(scope="function")
def logged_in_user(login_page_setup):
    """
    Fixture that provides a logged-in user session
    Returns the page object with an active session
    """
    page = login_page_setup["page"]
    login_page = login_page_setup["login_page"]
    home_page = login_page_setup["home_page"]
    
    login_page.login("test-pytest@example.com", "test123")
    assert login_page.is_logged_in(), "Failed to log in"

    return {
        "page": page,
        "home_page": home_page
    }

@pytest.fixture
def new_user_data(test_setup, request):
    """
    Fixture that creates a new user account and returns login credentials
    The logout behavior can be controlled using indirect parameterization
    
    Usage in tests:
      @pytest.mark.parametrize('new_user_data', [{'logout': False}], indirect=True)
      def test_example(new_user_data):
          # new_user_data will create a user and stay logged in
          
      def test_another_example(new_user_data):
          # By default will create a user and log out
    """
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    login_page = test_setup["login_page"]
    signup_info_page = test_setup["signup_info_page"]
    account_created_page = test_setup["account_created_page"]
    
    params = getattr(request, 'param', {})
    should_logout = params.get('logout', True)  

    assert home_page.is_home_page_visible()
    
    home_page.open_login_menu()
    try:
        page.wait_for_url('**/login', timeout=10000)
    except:
        pass 

    signup_name = fake.name()
    signup_email = fake.email()
    signup_password = fake.password()
    
    login_page.enter_signup_name(signup_name)
    login_page.enter_signup_email(signup_email)
    
    with page.expect_navigation(timeout=10000, url="**/signup"):
        login_page.click_signup_button()
    
    assert signup_info_page.verify_enter_account_info_is_visible()
    
    signup_info_page.select_gender('Mr')
    signup_info_page.enter_name(signup_name)
    signup_info_page.enter_password(signup_password)
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
    
    assert home_page.is_logged_in_as_visible()
    
    if should_logout:
        home_page.click_logout_account()
    
    yield (page, signup_email, signup_password, signup_name)

def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "test_setup" in item.funcargs:
            page = item.funcargs["test_setup"]["page"]
            allure.attach(
                page.screenshot(full_page=True),
                name=f"{item.nodeid}.png",
                attachment_type=allure.attachment_type.PNG
            )
        
@pytest.fixture(scope="session")
def faker():
    return fake
