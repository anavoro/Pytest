import pytest
import allure
from faker import Faker

@pytest.mark.login
@allure.feature("Login & Authentication")
@allure.story("Login with Invalid Credentials")
def test_login_with_invalid_credentials(login_page_setup):
    page = login_page_setup["page"]
    login_page = login_page_setup["login_page"]
    fake = Faker()

    email = fake.email()
    password = fake.password()
    login_page.login(email, password)

    email = fake.email()
    password = fake.password()
    login_page.login(email, password)

    assert login_page.wait_for_selector(login_page.login_error_message, timeout=5000)
    expected_error = 'Your email or password is incorrect!'
    assert login_page.get_error_message_text() == expected_error
