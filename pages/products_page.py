import re
from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
        expect(self.title).to_have_text("Products")
        expect(self.items).to_have_count(6)

    def sort_by(self, value: str):
        self.sort_dropdown.select_option(value)

    def get_names(self) -> list[str]:
        return self.item_names.all_text_contents()

    def get_prices(self) -> list[float]:
        texts = self.item_prices.all_text_contents()
        return [float(t.replace("$", "")) for t in texts]