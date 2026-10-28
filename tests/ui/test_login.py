import pytest
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.ui
def test_login_success(login_page, page):  # TC_LOGIN_001
    login_page.login("standard_user", "secret_sauce")
    ProductsPage(page).expect_loaded()


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "username, password, error",
    [
        ("standard_user", "wrong_pass", "Username and password do not match any user in this service"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ],
    ids=["TC_LOGIN_002-wrong-pass", "TC_LOGIN_004-no-user",
         "TC_LOGIN_005-no-pass", "TC_LOGIN_007-locked-user"],
)
def test_login_negative(login_page, username, password, error):
    login_page.login(username, password)
    login_page.expect_error(error)


@pytest.mark.regression
@pytest.mark.ui
def test_access_products_without_login(page, login_page):  # TC_LOGIN_011
    page.goto("/inventory.html")
    login_page.expect_error("You can only access '/inventory.html' when you are logged in.")