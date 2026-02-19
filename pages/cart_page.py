from playwright.sync_api import Page
from pages.base_page import BasePage

URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def navigate(self):
        super().navigate(URL)

    def get_cart_items(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def remove_item(self, name: str):
        item = self.page.locator(".cart_item").filter(has_text=name)
        item.locator("button").click()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
