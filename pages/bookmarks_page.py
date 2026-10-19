from playwright.sync_api import Page
import re

from pages.base_page import BasePage


class BookmarksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.my_divar_button = page.get_by_role("button", name=re.compile(r"دیوار من"))
        self.bookmarks_menu_item = page.get_by_text("نشان‌ها", exact=True)

    def open_from_menu(self):
        """Open bookmarks from My Divar menu (guest may see login modal)."""
        self.my_divar_button.click()
        self.bookmarks_menu_item.click()