import pytest

def test_register_and_login(test_setup, new_user_data):
    """
    Test case for registering a user and then logging in again
    Uses the default behavior of new_user_data fixture (logs out)
    """
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    login_page = test_setup["login_page"]
    account_deleted_page = test_setup["account_deleted_page"]
    
    _, email, password, name = new_user_data
    
    home_page.open_login_menu()
    
    page.wait_for_url('**/login', timeout=10000)

    login_page.login(email, password)
    assert home_page.is_logout_button_visible(), "Logout button not visible after login"
    
    home_page.click_delete_account()
    assert account_deleted_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"
    account_deleted_page.click_continue()
    
    assert home_page.is_home_page_visible(), "Home page is not visible after completing test"