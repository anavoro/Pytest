import pytest

@pytest.mark.login
def test_signup_with_same_email(login_page_setup):
    page = login_page_setup["page"]
    login_page = login_page_setup["login_page"]

    login_page.signup('Test_user', 'test-pytest@example.com')
 
    assert login_page.is_visible(login_page.signup_error_message)
    expected_error = 'Email Address already exist!'
    assert login_page.get_signup_error_message_text() == expected_error