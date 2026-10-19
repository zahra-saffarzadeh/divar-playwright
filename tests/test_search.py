import re
import pytest
from data.test_data import *
import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_search_with_results(home_with_tehran: HomePage):
    search_page = home_with_tehran.search(VALID_SEARCH_KEYWORD)

    expect(home_with_tehran.page).to_have_url(re.compile(r".*q=.*"))
    search_page.expect_results_visible()
    assert search_page.get_result_count() > 0


def test_search_with_no_results(home_with_tehran: HomePage):
    search_page = home_with_tehran.search(NO_RESULT_KEYWORD)
    search_page.expect_no_results()


def test_sort_by_cheapest(home_with_tehran: HomePage, page: Page):
    search_results_page = home_with_tehran.search(VALID_SEARCH_KEYWORD)
    search_results_page.open_sort_menu()
    search_results_page.select_sort_option("ارزان‌ترین")

    expect(page).to_have_url(re.compile(r".*sort=cheapest"))


def test_clear_search(home_with_tehran: HomePage):
    search_results_page = home_with_tehran.search(VALID_SEARCH_KEYWORD)
    search_results_page.clear_search()
    search_results_page.expect_search_cleared()


def test_search_suggestions(home_with_tehran: HomePage, page: Page):
    home_with_tehran.type_in_search(VALID_SEARCH_KEYWORD)
    expect(page.get_by_text(VALID_SEARCH_KEYWORD, exact=True).first).to_be_visible()
    expect(page.get_by_text("در موبایل").first).to_be_visible()


@pytest.mark.parametrize("keyword", SEARCH_KEYWORDS)
def test_search_multiple_keywords(home_with_tehran: HomePage, page: Page, keyword: str):
    search_page = home_with_tehran.search(keyword)

    expect(page).to_have_url(re.compile(r".*q=.*"))
    search_page.expect_results_visible()
    assert search_page.get_result_count() > 0