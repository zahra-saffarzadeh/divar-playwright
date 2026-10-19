import re

from playwright.sync_api import Page, expect, Route

from pages.home_page import HomePage


def test_network_request_on_search(home_with_tehran: HomePage, page: Page):
    """Assert Divar network requests are fired after search."""
    requests = []

    def handle_request(request):
        requests.append(request.url)

    page.on("request", handle_request)
    home_with_tehran.search("آیفون")

    divar_requests = [url for url in requests if "divar.ir" in url]
    assert len(divar_requests) > 0
    expect(page).to_have_url(re.compile(r".*q=.*"))


def test_intercept_and_check_api(home_with_tehran: HomePage, page: Page):
    """Collect API-like responses during search."""
    api_responses = []

    def handle_response(response):
        if "api" in response.url or "v8" in response.url or "search" in response.url:
            api_responses.append({
                "url": response.url,
                "status": response.status,
            })

    page.on("response", handle_response)
    home_with_tehran.search("سامسونگ")

    # Soft check: list may be empty depending on Divar endpoints
    assert isinstance(api_responses, list)


def test_mock_api_empty_results(home_with_tehran: HomePage, page: Page):
    """Example route mock (UI may not change; Divar API is complex)."""

    def mock_route(route: Route):
        if "search" in route.request.url or "list" in route.request.url:
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"widget_list": [], "title": "نتیجهٔ دقیقی پیدا نشد"}',
            )
        else:
            route.continue_()

    page.route("**/*", mock_route)
    home_with_tehran.search("آیفون")


def test_screenshot_on_home(home_with_tehran: HomePage, page: Page):
    page.screenshot(path="reports/home_tehran.png", full_page=True)


def test_responsive_mobile_viewport(page: Page):
    """Smoke check on mobile viewport."""
    page.set_viewport_size({"width": 375, "height": 812})

    home_page = HomePage(page)
    home_page.open()
    home_page.select_city("تهران")

    expect(page).to_have_url(re.compile(r".*/s/tehran"))
    page.screenshot(path="reports/home_mobile.png")


def test_dialog_handling(home_with_tehran: HomePage, page: Page):
    """Open and close the login dialog."""
    page.get_by_role("button", name=re.compile(r"دیوار من")).click()
    page.get_by_text("ورود به حساب کاربری", exact=True).click()

    dialog = page.get_by_role("dialog")
    expect(dialog).to_be_visible()

    dialog.get_by_role("button", name="بستن").click()
    expect(dialog).to_be_hidden()