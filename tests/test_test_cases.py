import pytest
import allure

@pytest.mark.other
@allure.feature("Other functionalities")
@allure.story("Verifying the test cases page visibility")
def test_test_cases(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    test_cases_page = test_setup["test_cases_page"]

    home_page.is_home_page_visible()

    home_page.navigate_to_test_cases()

    test_cases_page.verify_test_cases_loaded()