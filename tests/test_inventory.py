import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.product_detail_page import ProductDetailPage
from data.test_data import EXPECTED_PRODUCT_COUNT


@allure.feature("Product Catalog")
class TestInventory:

    @allure.story("Products display")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_products_displayed(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Verify all 6 products are listed"):
            assert inventory.get_item_count() == EXPECTED_PRODUCT_COUNT

    @allure.story("Sorting")
    def test_sort_name_az(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Sort by Name A→Z"):
            inventory.sort_by("az")
        with allure.step("Verify first product is alphabetically first"):
            names = inventory.get_product_names()
            assert names == sorted(names)

    @allure.story("Sorting")
    def test_sort_name_za(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Sort by Name Z→A"):
            inventory.sort_by("za")
        with allure.step("Verify first product is alphabetically last"):
            names = inventory.get_product_names()
            assert names == sorted(names, reverse=True)

    @allure.story("Sorting")
    def test_sort_price_low_high(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Sort by Price low→high"):
            inventory.sort_by("lohi")
        with allure.step("Verify prices are ascending"):
            prices = inventory.get_product_prices()
            assert prices == sorted(prices)

    @allure.story("Sorting")
    def test_sort_price_high_low(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Sort by Price high→low"):
            inventory.sort_by("hilo")
        with allure.step("Verify prices are descending"):
            prices = inventory.get_product_prices()
            assert prices == sorted(prices, reverse=True)

    @allure.story("Add to cart from listing")
    @pytest.mark.smoke
    def test_add_to_cart_from_listing(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Add first product to cart"):
            first_product = inventory.get_product_names()[0]
            inventory.add_to_cart_by_name(first_product)
        with allure.step("Verify cart badge shows 1"):
            assert inventory.get_cart_count() == 1

    @allure.story("Product detail page")
    def test_open_product_detail(self, logged_in):
        inventory = InventoryPage(logged_in)
        with allure.step("Click on first product name"):
            first_product = inventory.get_product_names()[0]
            inventory.open_product(first_product)
        with allure.step("Verify product detail page is shown"):
            detail = ProductDetailPage(logged_in)
            assert detail.get_product_name() == first_product
