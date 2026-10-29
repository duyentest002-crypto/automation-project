import re
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/cart\.html"))
        expect(self.title).to_have_text("Your Cart")
        expect(self.items).to_have_count(1)  # Assuming one item is added to cart

    def remove_item(self, item_name: str):
        item = self.page.locator(f".cart_item:has-text('{item_name}')")
        remove_button = item.locator("button:has-text('Remove')")
        remove_button.click()

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.checkout_button.click()