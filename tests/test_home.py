from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_divar_home_page(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.select_city("تهران")

    expect(page).to_have_title("دیوار تهران - آگهی های رایگان خرید، فروش و استخدام | دیوار")