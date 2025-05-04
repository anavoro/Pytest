from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        """
        Initializes the BasePage with the Playwright Page object.
        """
        self.page = page

    def navigate(self, url: str):
        """
        Navigates to the specified URL.
        """
        self.page.goto(url)

    def get_title(self) -> str:
        """
        Returns the title of the current page.
        """
        return self.page.title()

    def get_url(self) -> str:
        """
        Returns the URL of the current page.
        """
        return self.page.url

    def click(self, selector: str, timeout: int = 5000):
        """
        Clicks the element matching the selector.
        """
        self.page.click(selector, timeout=timeout)

    def fill(self, selector: str, text: str, timeout: int = 5000):
        """
        Fills the input field matching the selector with the given text.
        """
        self.page.fill(selector, text, timeout=timeout)

    def wait_for_selector(self, selector: str, state: str = 'visible', timeout: int = 5000):
        """
        Waits for the element matching the selector to be in the specified state.
        """
        self.page.wait_for_selector(selector, state=state, timeout=timeout)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """
        Checks if the element matching the selector is visible.
        """
        try:
            self.page.wait_for_selector(selector, state='visible', timeout=timeout)
            return True
        except:
            return False

    def get_text(self, selector: str, timeout: int = 5000) -> str:
        """
        Returns the text content of the element matching the selector.
        """
        self.page.wait_for_selector(selector, state='visible', timeout=timeout)
        return self.page.inner_text(selector, timeout=timeout)

