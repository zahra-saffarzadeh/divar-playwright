from playwright.sync_api import Page, expect

from pages.d_detail_page import AdDetailPage
from pages.bookmarks_page import BookmarksPage


def test_bookmark_button_visible_on_ad(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    ad_page.expect_bookmark_button_visible()


def test_guest_bookmark_opens_login(mobile_category, page: Page):
    """Guest click on bookmark should open login modal."""
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()
    ad_page.click_bookmark()

    login_dialog = page.get_by_role("dialog")
    expect(login_dialog).to_be_visible()
    expect(login_dialog.get_by_text("ورود به حساب کاربری")).to_be_visible()
    expect(login_dialog.get_by_placeholder("۰۹۱۲ ۱۲۳ ۴۵۶۷")).to_be_visible()


def test_guest_bookmarks_menu_opens_login(home_with_tehran, page: Page):
    """Guest opening bookmarks menu should open login modal."""
    bookmarks_page = BookmarksPage(page)
    bookmarks_page.open_from_menu()

    login_dialog = page.get_by_role("dialog")
    expect(login_dialog).to_be_visible()
    expect(login_dialog.get_by_text("ورود به حساب کاربری")).to_be_visible()