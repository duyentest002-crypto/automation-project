import re
import pytest
from playwright.sync_api import expect
from config import BASE_URL
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.ui
def test_logout_success(products_page, page):  # TC_LOGOUT_001
    # TODO: gọi logout
    products_page.logout()
    # TODO: tạo LoginPage(page)
    login_page = LoginPage(page)
    # TODO: assert nút Login hiển thị
    expect(login_page.login_button).to_be_visible()
    # TODO: assert ô Username và Password rỗng
    expect(login_page.username_input).to_have_value("")
    expect(login_page.password_input).to_have_value("")
    # TODO: assert URL là trang chủ
    expect(page).to_have_url(re.compile(re.escape(BASE_URL) + r"/?$"))