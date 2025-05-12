import pytest
import allure

@pytest.mark.login
@allure.feature("Login & Authentication")
@allure.story("Logout")
def test_user_logout(logged_in_user): 
    page = logged_in_user["page"]
    home_page = logged_in_user["home_page"]

    assert home_page.is_logout_button_visible()

    home_page.click_logout_account()

    assert home_page.is_signup_login_button_visible()
