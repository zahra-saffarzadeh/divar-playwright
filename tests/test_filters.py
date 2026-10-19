import re
from playwright.sync_api import Page, expect
from pages.filters_page import FiltersPage



def test_price_filter(mobile_category, page: Page):
    filters_page = FiltersPage(page)
    filters_page.set_price_filter(min_price="10000000", max_price="50000000")

    filters_page.expect_url_contains(r".*price=.*")
    filters_page.expect_results_visible()

def test_has_photo_filter(mobile_category, page: Page):
    filters_page = FiltersPage(page)
    filters_page.enable_has_photo()

    expect(page).to_have_url(re.compile(r".*has-photo=true.*"))
    filters_page.expect_results_visible()


def test_combined_filters(mobile_category, page: Page):
    filters_page = FiltersPage(page)
    filters_page.set_price_filter(min_price="5000000", max_price="100000000")
    filters_page.enable_has_photo()

    filters_page.expect_results_visible()
    assert filters_page.get_result_count() > 0