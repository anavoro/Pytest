from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.all_products_header = page.locator('h2.title.text-center:has-text("All Products")')
        self.products_list = page.locator('div.features_items')
        self.first_product_view_button = page.locator('a[href="/product_details/1"]').first

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
  