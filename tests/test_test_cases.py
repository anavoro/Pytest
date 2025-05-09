import pytest

@pytest.mark.other
def test_test_cases(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    test_cases_page = test_setup["test_cases_page"]

    home_page.is_home_page_visible()

    home_page.navigate_to_test_cases()

    test_cases_page.verify_test_cases_loaded()