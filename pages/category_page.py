from playwright.sync_api import Page, expect
import re

from pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.result_cards = page.get_by_role("article")
        self.page_heading = page.get_by_role("heading", level=1)

        # Scope to category sidebar to avoid matching ad links
        self.sidebar = page.get_by_role("complementary", name="دسته‌ها و فیلترها")

    def open_category(self, category_name: str):
        """Open a main category from the sidebar."""
        self.sidebar.get_by_role("link", name=re.compile(category_name)).first.click()

    def open_subcategory(self, subcategory_name: str):
        """Open a subcategory (exact match, e.g. موبایل)."""
        self.sidebar.get_by_role("link", name=subcategory_name, exact=True).click()

    def get_result_count(self) -> int:
        return self.result_cards.count()

    def expect_results_visible(self):
        expect(self.result_cards.first).to_be_visible()

    def expect_url_contains(self, path: str):
        expect(self.page).to_have_url(re.compile(path))

    def expect_title_contains(self, text: str):
        expect(self.page).to_have_title(re.compile(text))