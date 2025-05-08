from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.page = page
        self.all_products_header = page.locator('h2.title.text-center:has-text("All Products")')
        self.products_list = page.locator('div.features_items')
        self.first_product_view_button = page.locator('a[href="/product_details/1"]').first
        self.search_input = "#search_product"
        self.search_button = "#submit_search"
        self.searched_products_title = 'h2.title:has-text("Searched Products")'
        self.product_name_elements = ".productinfo p"

    def verify_products_page_visible(self):
        expect(self.all_products_header).to_be_visible()

    def verify_products_list_visible(self):
        """Assert that products list is visible"""
        expect(self.products_list).to_be_visible()

    def click_view_first_product(self):
        self.page.wait_for_load_state('domcontentloaded')
        self.first_product_view_button.wait_for(state='visible', timeout=5000)
        self.first_product_view_button.scroll_into_view_if_needed()
        self.first_product_view_button.click()
    
    def wait_for_all_products_loaded(self):
        self.page.wait_for_selector(self.product_name_elements)

    def get_all_product_names(self):
        self.wait_for_all_products_loaded()
        return self.page.locator(self.product_name_elements).all_text_contents()

    def search_for_product(self, product_name: str):
        self.page.fill(self.search_input, product_name)
        self.page.click(self.search_button)
        self.page.wait_for_selector(self.searched_products_title)

    def is_searched_products_title_visible(self):
        return self.page.locator(self.searched_products_title).is_visible()

    def get_search_results_names(self):
        return self.page.locator(self.product_name_elements).all_text_contents()