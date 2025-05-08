from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def click(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, state='visible', timeout=timeout)
        self.page.click(selector, timeout=timeout)


    def fill(self, selector: str, text: str, timeout: int = 5000):
        self.page.fill(selector, text, timeout=timeout)

    def wait_for_selector(self, selector: str, state: str = 'visible', timeout: int = 5000):
        self.page.wait_for_selector(selector, state=state, timeout=timeout)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, state='visible', timeout=timeout)
            return True
        except:
            return False

    def get_text(self, selector: str, timeout: int = 5000) -> str:
        self.page.wait_for_selector(selector, state='visible', timeout=timeout)
        return self.page.inner_text(selector, timeout=timeout)
