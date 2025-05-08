from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.product_name = page.locator('h2:has-text("Blue Top")')
        self.product_category = page.locator('p:has-text("Category:")')
        self.product_price = page.locator(".product-information span > span", has_text="Rs. 500")
        self.product_availability = page.locator('b:has-text("Availability:")')
        self.product_condition = page.locator('b:has-text("Condition:")')
        self.product_brand = page.locator('b:has-text("Brand:")')

    def verify_product_detail_page_loaded(self):
        self.page.wait_for_load_state('domcontentloaded')
        assert "product_details" in self.page.url, "Not on product detail page"

    def verify_all_product_details_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.product_category).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()
