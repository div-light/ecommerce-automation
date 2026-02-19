import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from data.test_data import CHECKOUT_INFO


@allure.feature("Checkout")
class TestCheckout:

    @allure.story("Full checkout flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_full_checkout_flow(self, logged_in):
        info = CHECKOUT_INFO["valid"]

        with allure.step("Add a product to cart"):
            inventory = InventoryPage(logged_in)
            name = inventory.get_product_names()[0]
            inventory.add_to_cart_by_name(name)
            inventory.go_to_cart()

        with allure.step("Proceed to checkout"):
            cart = CartPage(logged_in)
            assert name in cart.get_cart_items()
            cart.checkout()

        with allure.step("Fill in checkout information"):
            checkout_info = CheckoutInfoPage(logged_in)
            checkout_info.fill_info(
                info["first_name"], info["last_name"], info["postal_code"]
            )
            checkout_info.continue_checkout()

        with allure.step("Review order and finish"):
            overview = CheckoutOverviewPage(logged_in)
            assert name in overview.get_items()
            overview.finish()

        with allure.step("Verify order confirmation"):
            complete = CheckoutCompletePage(logged_in)
            assert "Thank you" in complete.get_header()

    @allure.story("Checkout validation")
    def test_checkout_missing_first_name(self, logged_in):
        with allure.step("Add item and reach checkout info page"):
            inventory = InventoryPage(logged_in)
            inventory.add_to_cart_by_name(inventory.get_product_names()[0])
            inventory.go_to_cart()
            CartPage(logged_in).checkout()

        with allure.step("Submit form without first name"):
            checkout_info = CheckoutInfoPage(logged_in)
            checkout_info.fill_info("", "Doe", "12345")
            checkout_info.continue_checkout()

        with allure.step("Verify first name error"):
            assert checkout_info.is_error_visible()
            assert "First Name is required" in checkout_info.get_error_message()

    @allure.story("Checkout validation")
    def test_checkout_missing_last_name(self, logged_in):
        with allure.step("Add item and reach checkout info page"):
            inventory = InventoryPage(logged_in)
            inventory.add_to_cart_by_name(inventory.get_product_names()[0])
            inventory.go_to_cart()
            CartPage(logged_in).checkout()

        with allure.step("Submit form without last name"):
            checkout_info = CheckoutInfoPage(logged_in)
            checkout_info.fill_info("John", "", "12345")
            checkout_info.continue_checkout()

        with allure.step("Verify last name error"):
            assert checkout_info.is_error_visible()
            assert "Last Name is required" in checkout_info.get_error_message()

    @allure.story("Checkout validation")
    def test_checkout_missing_zip(self, logged_in):
        with allure.step("Add item and reach checkout info page"):
            inventory = InventoryPage(logged_in)
            inventory.add_to_cart_by_name(inventory.get_product_names()[0])
            inventory.go_to_cart()
            CartPage(logged_in).checkout()

        with allure.step("Submit form without postal code"):
            checkout_info = CheckoutInfoPage(logged_in)
            checkout_info.fill_info("John", "Doe", "")
            checkout_info.continue_checkout()

        with allure.step("Verify postal code error"):
            assert checkout_info.is_error_visible()
            assert "Postal Code is required" in checkout_info.get_error_message()

    @allure.story("Order confirmation message")
    @pytest.mark.regression
    def test_order_confirmation_message(self, logged_in):
        info = CHECKOUT_INFO["valid"]

        with allure.step("Complete the full checkout flow"):
            inventory = InventoryPage(logged_in)
            inventory.add_to_cart_by_name(inventory.get_product_names()[0])
            inventory.go_to_cart()
            CartPage(logged_in).checkout()
            checkout_info = CheckoutInfoPage(logged_in)
            checkout_info.fill_info(
                info["first_name"], info["last_name"], info["postal_code"]
            )
            checkout_info.continue_checkout()
            CheckoutOverviewPage(logged_in).finish()

        with allure.step("Verify confirmation header and body text"):
            complete = CheckoutCompletePage(logged_in)
            assert complete.get_header() == "Thank you for your order!"
            assert "dispatched" in complete.get_body_text().lower()
