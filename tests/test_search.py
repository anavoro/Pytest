import random

def test_search_random_product(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]
    products_page = test_setup["products_page"]

    home_page.navigate_to_products()

    products_page.verify_products_page_visible()
    product_names = products_page.get_all_product_names()
    assert product_names, "No product names found"

    selected_name = random.choice(product_names)
    products_page.search_for_product(selected_name)

    assert products_page.is_searched_products_title_visible()
    results = products_page.get_search_results_names()
    assert any(selected_name.lower() in r.lower() for r in results), \
        f"Search result does not include '{selected_name}'"
