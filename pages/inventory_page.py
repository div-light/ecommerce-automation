from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def navigate(self):
        super().navigate("/inventory.html")

    def get_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_product_prices(self) -> list[float]:
        raw = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    def sort_by(self, value: str):
        self.sort_dropdown.select_option(value)

    def add_to_cart_by_name(self, name: str):
        item = self.page.locator(".inventory_item").filter(has_text=name)
        item.locator("button").click()

    def remove_from_cart_by_name(self, name: str):
        item = self.page.locator(".inventory_item").filter(has_text=name)
        item.locator("button").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_icon.click()

    def open_product(self, name: str):
        self.page.locator(".inventory_item_name").filter(has_text=name).click()

    def get_item_count(self) -> int:
        return self.inventory_items.count()
