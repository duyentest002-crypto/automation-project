import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from api.booking_client import BookingClient, build_booking
from config import ADMIN_USER, ADMIN_PASSWORD
from pages.products_page import ProductsPage
import base64
from pytest_html import extras


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

@pytest.fixture(scope="session")
def booking_client():
    return BookingClient()


@pytest.fixture(scope="session")
def token(booking_client):
    resp = booking_client.create_token(ADMIN_USER, ADMIN_PASSWORD)
    assert resp.status_code == 200
    return resp.json()["token"]


@pytest.fixture
def new_booking(booking_client, token):
    payload = build_booking()
    resp = booking_client.create_booking(payload)
    assert resp.status_code == 200
    booking_id = resp.json()["bookingid"]
    yield {"id": booking_id, "payload": payload}
    booking_client.delete_booking(booking_id, token)  # dọn dẹp, bỏ qua kết quả

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")  # chỉ test UI mới có "page"
        if page:
            try:
                png = page.screenshot()
                img = base64.b64encode(png).decode()
                report.extras = getattr(report, "extras", []) + [extras.png(img)]
            except Exception:
                pass  # trang đã đóng thì bỏ qua, không làm hỏng báo cáo