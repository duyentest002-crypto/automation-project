import pytest


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "option, field, reverse",
    [
        ("az", "names", False),
        ("za", "names", True),
        ("lohi", "prices", False),
        ("hilo", "prices", True),
    ],
    ids=[
        "TC_PROD_002-name-az",
        "TC_PROD_003-name-za",
        "TC_PROD_004-price-lohi",
        "TC_PROD_005-price-hilo",
    ],
)
def test_sort_products(products_page, option, field, reverse):
    products_page.sort_by(option)

    if field == "names":
        actual = products_page.get_names()
    else:
        actual = products_page.get_prices()

    assert actual == sorted(actual, reverse=reverse)