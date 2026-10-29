import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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

@pytest.fixture
def checkout_page(products_page, page):
    # TODO: thêm "Sauce Labs Backpack", mở giỏ hàng
    products_page.add_to_cart("Sauce Labs Backpack")
    products_page.open_cart()
    cart_page = CartPage(page)
    cart_page.checkout()
    return CheckoutPage(page)