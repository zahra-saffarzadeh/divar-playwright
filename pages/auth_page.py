from playwright.sync_api import Page, expect
import re

from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.my_divar_button = page.get_by_role("button", name=re.compile(r"دیوار من"))
        self.login_menu_item = page.get_by_text("ورود به حساب کاربری", exact=True)

        # Login modal elements
        self.login_modal = page.get_by_role("dialog")
        self.phone_input = page.get_by_placeholder("۰۹۱۲ ۱۲۳ ۴۵۶۷")
        self.next_button = page.get_by_role("button", name="بعدی", exact=True)
        self.close_button = page.get_by_role("button", name="بستن")
        self.invalid_phone_error = page.get_by_text("شمارهٔ موبایل نامعتبر است")

    def open_login(self):
        """Open login modal via My Divar menu."""
        self.my_divar_button.click()
        self.login_menu_item.click()

    def enter_phone(self, phone: str):
        self.phone_input.fill(phone)

    def submit_phone(self):
        self.next_button.click()

    def expect_login_modal_visible(self):
        expect(self.login_modal).to_be_visible()
        expect(self.phone_input).to_be_visible()

    def expect_invalid_phone_error(self):
        expect(self.invalid_phone_error).to_be_visible()

    def close_login_modal(self):
        self.close_button.click()