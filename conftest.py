import pytest
from pages.login_page import LoginPage
from data.test_data import USERS


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def logged_in(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login(USERS["standard"]["username"], USERS["standard"]["password"])
    return page
