from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class TestCasesPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)  
        self.test_cases_header = page.locator("h2.title.text-center", has_text="Test Cases")

    def verify_test_cases_loaded(self):
        expect(self.test_cases_header).to_be_visible()
        expect(self.test_cases_header).to_have_text("Test Cases")