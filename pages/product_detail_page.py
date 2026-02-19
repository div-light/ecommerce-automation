from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_name = page.locator(".inventory_details_name")
        self.product_price = page.locator(".inventory_details_price")
        self.add_to_cart_button = page.locator("#add-to-cart")
        self.back_button = page.locator("#back-to-products")

    def get_product_name(self) -> str:
        return self.product_name.inner_text()

    def get_product_price(self) -> str:
        return self.product_price.inner_text()

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def back_to_products(self):
        self.back_button.click()
