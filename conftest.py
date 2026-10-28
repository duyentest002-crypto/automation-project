import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def products_page(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    pp = ProductsPage(page)
    pp.expect_loaded()
    return pp