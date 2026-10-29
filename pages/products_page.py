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
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

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

    def add_to_cart(self, item_name: str):
        item = self.page.locator(f".inventory_item:has-text('{item_name}')")
        add_button = item.locator("button:has-text('Add to cart')")
        add_button.click()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_button.click()