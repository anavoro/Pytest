from playwright.sync_api import Page, expect

class TestCasesPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.test_cases_header = page.locator("h2.title.text-center", has_text="Test Cases")

    def verify_test_cases_loaded(self):
        expect(self.test_cases_header).to_be_visible()
        expect(self.test_cases_header).to_have_text("Test Cases")