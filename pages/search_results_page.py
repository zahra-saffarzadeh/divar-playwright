import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Placeholder changes after category search (e.g. "جستجو در موبایل")
        self.search_box = page.get_by_role("textbox", name=re.compile(r"جستجو در"))

        self.result_cards = page.get_by_role("article")
        self.result_titles = page.get_by_role("heading", level=2)
        self.no_result_message = page.get_by_text("نتیجهٔ دقیقی پیدا نشد")

        self.sort_button = page.get_by_role("button", name="جدیدترین")
        self.clear_search_button = page.get_by_role("button", name="حذف کردن")

    def get_result_count(self) -> int:
        return self.result_cards.count()

    def get_first_result_title(self) -> str:
        return self.result_titles.first.inner_text()

    def open_sort_menu(self):
        self.sort_button.click()

    def select_sort_option(self, option: str):
        self.page.get_by_role("link", name=option).click()

    def expect_results_visible(self):
        expect(self.result_cards.first).to_be_visible()

    def expect_no_results(self):
        expect(self.no_result_message).to_be_visible()
        assert self.get_result_count() == 0

    def clear_search(self):
        self.clear_search_button.click()

    def expect_search_cleared(self):
        expect(self.search_box).to_have_value("")