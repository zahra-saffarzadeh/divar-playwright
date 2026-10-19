import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.category_page import CategoryPage


SCREENSHOT_DIR = Path("reports/screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            test_name = item.name.replace("/", "_").replace("\\", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = SCREENSHOT_DIR / f"{test_name}_{timestamp}.png"
            page.screenshot(path=str(path), full_page=True)


@pytest.fixture
def home_with_tehran(page: Page) -> HomePage:
    """هر تستی که صفحه اصلی + تهران می‌خواهد"""
    home = HomePage(page)
    home.open()
    home.select_city("تهران")
    return home

@pytest.fixture
def category_page(home_with_tehran: HomePage, page: Page) -> CategoryPage:
    return CategoryPage(page)

@pytest.fixture
def mobile_category(home_with_tehran: HomePage, page: Page) -> CategoryPage:
    """مستقیم وارد دسته موبایل می‌شود"""
    category = CategoryPage(page)
    category.open_category("کالای دیجیتال")
    category.open_subcategory("موبایل و تبلت")
    category.open_subcategory("موبایل")
    return category