import pytest
import allure
import os

@pytest.mark.other
@allure.feature("Other functionalities")
@allure.story("Contact Us Form Submission")
def test_contact_us_form(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    contact_us_page = test_setup["contact_us_page"]
    
    assert home_page.is_home_page_visible()
    
    home_page.navigate_to_contact_us()

    assert contact_us_page.is_contact_page_visible()
    assert 'contact_us' in page.url
    
    contact_us_page.fill_contact_form(
        name="Test User",
        email="test_user@example.com",
        subject="Test Contact Form",
        message="This is a test message for the contact form."
    )

    test_file_path = os.path.join("utils", "test_upload.txt")
    with open(test_file_path, "w") as f:
       f.write("This is a test file for upload.")
    
    contact_us_page.upload_file(test_file_path)
    
    contact_us_page.handle_alert()
    
    contact_us_page.verify_success_message()

    contact_us_page.click_home_button()

    assert home_page.is_home_page_visible()
    