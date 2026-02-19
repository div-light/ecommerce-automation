from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = page.locator(".complete-header")
        self.body_text = page.locator(".complete-text")
        self.back_button = page.locator("#back-to-products")

    def get_header(self) -> str:
        return self.header.inner_text()

    def get_body_text(self) -> str:
        return self.body_text.inner_text()

    def back_to_home(self):
        self.back_button.click()
