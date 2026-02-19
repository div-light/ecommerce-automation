from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")

    def get_items(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_total_text(self) -> str:
        return self.total_label.inner_text()

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def finish(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()
