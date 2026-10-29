import re
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.error_message = page.locator("[data-test='error']")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-one\.html"))
        expect(self.title).to_have_text("Checkout: Your Information")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    def expect_error(self, message: str):
        expect(self.error_message).to_contain_text(message)

    def expect_complete_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/checkout-complete\.html"))
        expect(self.title).to_have_text("Checkout: Complete!")

    def get_item_total(self) -> float:
        item_total_text = self.page.locator(".summary_subtotal_label").inner_text()
        return float(item_total_text.split("$")[1])

    def get_tax(self) -> float:
        tax_text = self.page.locator(".summary_tax_label").inner_text()
        return float(tax_text.split("$")[1])

    def get_total(self) -> float:
        total_text = self.page.locator(".summary_total_label").inner_text()
        return float(total_text.split("$")[1])