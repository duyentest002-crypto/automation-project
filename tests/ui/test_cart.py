import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.ui
def test_add_one_product(products_page):  # TC_CART_001
    names = products_page.get_names()[:1]  # hàm đã có sẵn
    products_page.add_to_cart(names[0])
    expect(products_page.cart_badge).to_have_text("1")



@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize("count", [1, 3, 6])
def test_add_many_products(products_page, count):  # TC_CART_002
    names = products_page.get_names()[:count]   # hàm đã có sẵn
    # TODO: thêm từng sản phẩm trong names (vòng lặp for)
    for name in names:
        products_page.add_to_cart(name)
    # TODO: assert badge có chữ str(count)
    expect(products_page.cart_badge).to_have_text(str(count))


@pytest.mark.regression
@pytest.mark.ui
def test_remove_product_in_cart(products_page, page):  # TC_CART_005
    # TODO: thêm 2 sản phẩm
    names = products_page.get_names()[:2]
    for name in names:
        products_page.add_to_cart(name)

    # TODO: mở giỏ hàng, tạo CartPage(page)
    cart_page = CartPage(page)
    cart_page.open()

    # TODO: xóa 1 sản phẩm
    cart_page.remove_item(names[0])

    # TODO: assert giỏ chỉ còn 1 dòng, đúng sản phẩm còn lại, badge là "1"
    cart_page.expect_loaded()
    expect(cart_page.items).to_have_count(1)