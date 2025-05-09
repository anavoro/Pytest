import pytest

@pytest.mark.login
@pytest.mark.parametrize('new_user_data', [{'logout': False}], indirect=True)
def test_register_user(test_setup, new_user_data):
    """
    Test case for registering a user and verifying account creation
    Uses the new_user_data fixture with logout=False to stay logged in
    """
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    account_deleted_page = test_setup["account_deleted_page"]
    
    _, email, password, name = new_user_data
    
    assert home_page.is_logged_in_as_visible(), f"'Logged in as {name}' is not visible"
    
    home_page.click_delete_account()
    assert account_deleted_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"
    account_deleted_page.click_continue()

    assert home_page.is_home_page_visible(), "Home page is not visible after completing test"