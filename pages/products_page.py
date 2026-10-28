import re
from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
        expect(self.title).to_have_text("Products")
        expect(self.items).to_have_count(6)