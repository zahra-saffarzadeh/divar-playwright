from playwright.sync_api import Page
from pages.ad_detail_page import AdDetailPage


def test_open_ad(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    ad_page.expect_url_is_ad_detail()
    ad_page.expect_title_visible()


def test_ad_title_and_price(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    title = ad_page.get_title()
    assert len(title.strip()) > 0
    ad_page.expect_price_visible()


def test_ad_description(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()
    ad_page.expect_description_visible()


def test_ad_contact_and_chat(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    ad_page.expect_contact_button_visible()
    ad_page.expect_chat_button_visible()


def test_ad_share_and_bookmark(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    ad_page.expect_share_button_visible()
    ad_page.expect_bookmark_button_visible()


def test_ad_location(mobile_category, page: Page):
    ad_page = AdDetailPage(page)
    ad_page.open_first_ad_from_list()

    ad_page.expect_location_visible()