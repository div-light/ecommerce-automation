import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("Shopping Cart")
class TestCart:

    @allure.story("Add single item")
    @pytest.mark.smoke
    def test_add_single_item(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Add one product to cart"):
            name = inventory.get_product_names()[0]
            inventory.add_to_cart_by_name(name)
        with allure.step("Navigate to cart"):
            inventory.go_to_cart()
        with allure.step("Verify the item is in the cart"):
            cart = CartPage(logged_in)
            assert name in cart.get_cart_items()

    @allure.story("Add multiple items")
    def test_add_multiple_items(self, logged_in):
        inventory = InventoryPage(logged_in)
        names = inventory.get_product_names()
        with allure.step("Add first two products to cart"):
            inventory.add_to_cart_by_name(names[0])
            inventory.add_to_cart_by_name(names[1])
        with allure.step("Navigate to cart"):
            inventory.go_to_cart()
        with allure.step("Verify both items appear in cart"):
            cart = CartPage(logged_in)
            cart_items = cart.get_cart_items()
            assert names[0] in cart_items
            assert names[1] in cart_items
            assert cart.get_item_count() == 2

    @allure.story("Remove item")
    def test_remove_item(self, logged_in):
        inventory = InventoryPage(logged_in)
        names = inventory.get_product_names()
        with allure.step("Add two items to cart"):
            inventory.add_to_cart_by_name(names[0])
            inventory.add_to_cart_by_name(names[1])
            inventory.go_to_cart()
        with allure.step("Remove the first item"):
            cart = CartPage(logged_in)
            cart.remove_item(names[0])
        with allure.step("Verify first item is gone, second remains"):
            assert cart.get_item_count() == 1
            assert names[0] not in cart.get_cart_items()
            assert names[1] in cart.get_cart_items()

    @allure.story("Cart persists after navigation")
    def test_cart_persists_navigation(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Add item and navigate away"):
            name = inventory.get_product_names()[0]
            inventory.add_to_cart_by_name(name)
            inventory.go_to_cart()
        with allure.step("Return to inventory"):
            cart = CartPage(logged_in)
            cart.continue_shopping()
        with allure.step("Verify cart badge still shows 1"):
            assert inventory.get_cart_count() == 1

    @allure.story("Continue shopping")
    def test_continue_shopping(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Go to cart"):
            inventory.go_to_cart()
        with allure.step("Click Continue Shopping"):
            cart = CartPage(logged_in)
            cart.continue_shopping()
        with allure.step("Verify user is back on inventory page"):
            assert logged_in.url.endswith("/inventory.html")
