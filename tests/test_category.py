import re
import pytest
from playwright.sync_api import Page, expect
from pages.category_page import CategoryPage
from data.test_data import CATEGORIES


@pytest.mark.parametrize("category_name, url_part", CATEGORIES)
def test_open_category(category_page: CategoryPage, category_name: str, url_part: str):
    category_page.open_category(category_name)

    category_page.expect_url_contains(rf".*/s/tehran/{url_part}")
    category_page.expect_results_visible()
    assert category_page.get_result_count() > 0


def test_open_subcategory(category_page: CategoryPage):
    category_page.open_category("کالای دیجیتال")
    category_page.expect_url_contains(r".*/s/tehran/electronic-devices")

    category_page.open_subcategory("موبایل و تبلت")
    category_page.expect_url_contains(r".*/s/tehran/mobile-tablet")

    category_page.open_subcategory("موبایل")
    category_page.expect_url_contains(r".*/s/tehran/mobile-phones")
    category_page.expect_results_visible()


def test_category_page_title(category_page: CategoryPage):
    category_page.open_category("وسایل نقلیه")

    category_page.expect_title_contains(r"وسایل نقلیه|خودرو")
    category_page.expect_url_contains(r".*/s/tehran/vehicles")


def test_browser_back_navigation(category_page: CategoryPage, page: Page):
    category_page.open_category("املاک")
    expect(page).to_have_url(re.compile(r".*/s/tehran/real-estate"))
    page.go_back()
    expect(page).to_have_url(re.compile(r".*/s/tehran/?$"))