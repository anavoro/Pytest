import pytest
import allure

@pytest.mark.product
@allure.feature("Products")
@allure.story("Verify product list and product details visibility")
def test_products_and_details(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    products_page = test_setup["products_page"]
    product_details_page = test_setup["product_details_page"]

    assert home_page.is_home_page_visible()

    home_page.navigate_to_products()
    products_page.verify_products_page_visible()
    products_page.verify_products_list_visible()
    products_page.click_view_first_product()
    
    product_details_page.verify_product_detail_page_loaded()
    product_details_page.verify_all_product_details_visible()
