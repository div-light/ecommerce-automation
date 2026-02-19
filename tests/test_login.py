import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import USERS


@allure.feature("Authentication")
class TestLogin:

    @allure.story("Valid login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_valid_login(self, login_page):
        with allure.step("Log in with standard_user credentials"):
            login_page.login(
                USERS["standard"]["username"],
                USERS["standard"]["password"],
            )
        with allure.step("Verify inventory page is shown"):
            inventory = InventoryPage(login_page.page)
            assert login_page.page.url.endswith("/inventory.html")
            assert inventory.get_item_count() > 0

    @allure.story("Locked-out user")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_locked_out_user(self, login_page):
        with allure.step("Attempt login with locked_out_user"):
            login_page.login(
                USERS["locked"]["username"],
                USERS["locked"]["password"],
            )
        with allure.step("Verify error message is shown"):
            assert login_page.is_error_visible()
            assert "locked out" in login_page.get_error_message().lower()

    @allure.story("Invalid credentials")
    def test_invalid_username(self, login_page):
        with allure.step("Login with wrong username"):
            login_page.login("wrong_user", "secret_sauce")
        with allure.step("Verify error message appears"):
            assert login_page.is_error_visible()
            assert "Username and password do not match" in login_page.get_error_message()

    @allure.story("Invalid credentials")
    def test_invalid_password(self, login_page):
        with allure.step("Login with wrong password"):
            login_page.login("standard_user", "wrong_password")
        with allure.step("Verify error message appears"):
            assert login_page.is_error_visible()

    @allure.story("Empty credentials")
    def test_empty_credentials(self, login_page):
        with allure.step("Click login without entering credentials"):
            login_page.login("", "")
        with allure.step("Verify username required error"):
            assert login_page.is_error_visible()
            assert "Username is required" in login_page.get_error_message()

    @allure.story("Empty password")
    def test_empty_password(self, login_page):
        with allure.step("Enter username but no password"):
            login_page.login("standard_user", "")
        with allure.step("Verify password required error"):
            assert login_page.is_error_visible()
            assert "Password is required" in login_page.get_error_message()

    @allure.story("Performance glitch user")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_performance_glitch_user(self, login_page):
        with allure.step("Login with performance_glitch_user"):
            login_page.login(
                USERS["glitch"]["username"],
                USERS["glitch"]["password"],
            )
        with allure.step("Verify inventory page eventually loads"):
            login_page.page.wait_for_url("**/inventory.html", timeout=10000)
            assert login_page.page.url.endswith("/inventory.html")
