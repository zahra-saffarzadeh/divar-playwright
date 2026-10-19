from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class HomePage(BasePage):
    URL = "https://divar.ir"

    def __init__(self, page: Page):
        super().__init__(page)

        self.search_box = page.get_by_placeholder("جستجو در همهٔ آگهی‌ها")
        self.city_heading = page.get_by_role("heading")
        self.clear_search_button = page.get_by_role("button", name="حذف کردن")

    def open(self):
        super().open(self.URL)

    def select_city(self, city: str):
        self.page.get_by_role("heading", name=city).click()

    def search(self, text: str) -> SearchResultsPage:
        """Fill search, submit, and return results page."""
        self.search_box.fill(text)
        self.search_box.press("Enter")
        return SearchResultsPage(self.page)

    def type_in_search(self, text: str):
        """Type only (no Enter) to show search suggestions."""
        self.search_box.click()
        self.search_box.fill(text)

    def clear_search(self):
        self.clear_search_button.click()

    def get_search_value(self) -> str:
        return self.search_box.input_value()