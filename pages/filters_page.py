from playwright.sync_api import Page, expect
import re

from pages.base_page import BasePage


class FiltersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = page.get_by_role("complementary", name="دسته‌ها و فیلترها")
        self.result_cards = page.get_by_role("article")

        # Stable ids on Divar price fields
        self.price_min_input = page.locator("#price-minimum")
        self.price_max_input = page.locator("#price-maximum")

        self.has_photo_switch = page.get_by_role("switch", name="عکس‌دار")

    def set_price_filter(self, min_price: str = None, max_price: str = None):
        if min_price:
            self.price_min_input.click()
            self.price_min_input.fill(min_price)
            self.price_min_input.press("Enter")

        if max_price:
            self.price_max_input.click()
            self.price_max_input.fill(max_price)
            self.price_max_input.press("Enter")

        self.page.wait_for_load_state("networkidle")

    def enable_has_photo(self):
        # Input is visually hidden; click the label instead
        self.page.locator("#has-photo").get_by_text("عکس‌دار", exact=True).click()
        self.page.wait_for_load_state("networkidle")

    def disable_has_photo(self):
        self.page.locator("#has-photo").get_by_text("عکس‌دار", exact=True).click()
        self.page.wait_for_load_state("networkidle")

    def is_has_photo_enabled(self) -> bool:
        return self.has_photo_switch.is_checked()

    def get_result_count(self) -> int:
        return self.result_cards.count()

    def expect_results_visible(self):
        expect(self.result_cards.first).to_be_visible()

    def expect_url_contains(self, text: str):
        expect(self.page).to_have_url(re.compile(text))