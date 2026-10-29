import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_checkout_success(checkout_page, page):  # TC_CHK_001
    # TODO: điền thông tin hợp lệ -> continue -> finish
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    # TODO: assert màn hình Complete
    checkout_page.expect_complete_loaded()
    # TODO: assert badge giỏ hàng biến mất
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "first, last, postal, error",
    [
        # TODO: 3 bộ dữ liệu, mỗi bộ bỏ trống đúng 1 trường
        ("", "Doe", "12345", "Error: First Name is required"),
        ("John", "", "12345", "Error: Last Name is required"),
        ("John", "Doe", "", "Error: Postal Code is required"),

    ],
    ids=["TC_CHK_002-no-first", "TC_CHK_003-no-last", "TC_CHK_004-no-postal"],
)
def test_checkout_required_fields(checkout_page, page, first, last, postal, error):
    # TODO: điền, bấm continue
    checkout_page.fill_information(first, last, postal)
    checkout_page.continue_checkout()
    checkout_page.expect_error(error)

    # TODO: assert thông báo lỗi
    checkout_page.expect_error(error)

    # TODO: assert vẫn ở bước nhập thông tin
    checkout_page.expect_loaded()



@pytest.mark.regression
@pytest.mark.ui
def test_checkout_totals(checkout_page):  # TC_CHK_007
    # TODO: điền thông tin hợp lệ -> continue
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.continue_checkout()

    # TODO: lấy item total, tax, total
    item_total = checkout_page.get_item_total()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    # TODO: assert 3 con số
    assert item_total > 0
    assert tax > 0
    assert total > 0