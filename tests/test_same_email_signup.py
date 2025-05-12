import pytest
import allure 
from utils.test_data import Data

@pytest.mark.login
@allure.feature("Login & Authentication")
@allure.story("Signup using the email that is already in the system")
def test_signup_with_same_email(login_page_setup):
    page = login_page_setup["page"]
    login_page = login_page_setup["login_page"]

    login_page.signup(Data.NAME, Data.EMAIL)
 
    assert login_page.is_visible(login_page.signup_error_message)
    expected_error = 'Email Address already exist!'
    assert login_page.get_signup_error_message_text() == expected_error