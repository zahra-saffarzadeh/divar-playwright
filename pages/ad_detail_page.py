from playwright.sync_api import Page, expect
import re

from pages.base_page import BasePage


class AdDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.ad_title = page.get_by_role("heading", level=1)

        # Primary action buttons on ad page
        self.contact_button = page.locator("button.post-actions__get-contact")
        self.chat_button = page.get_by_role("button", name=re.compile(r"چت"))
        self.bookmark_button = page.get_by_role("button", name="نشان کردن")
        self.share_button = page.get_by_role("button", name="اشتراک گذاری")

        self.price_label = page.get_by_text("قیمت", exact=True)
        self.price_value = page.get_by_text(re.compile(r"تومان|توافقی"))

        self.description_heading = page.get_by_role("heading", name="توضیحات")

        # Location is shown as a button, e.g. "۲ هفته پیش در تهران..."
        self.location_text = page.get_by_role("button", name=re.compile(r"پیش در"))

    def open_first_ad_from_list(self):
        self.page.get_by_role("article").first.click()

    def get_title(self) -> str:
        return self.ad_title.inner_text()

    def expect_title_visible(self):
        expect(self.ad_title).to_be_visible()

    def expect_url_is_ad_detail(self):
        expect(self.page).to_have_url(re.compile(r".*/v/.*"))

    def expect_contact_button_visible(self):
        expect(self.contact_button).to_be_visible()

    def expect_chat_button_visible(self):
        expect(self.chat_button).to_be_visible()

    def expect_price_visible(self):
        expect(self.price_label).to_be_visible()
        expect(self.price_value.first).to_be_visible()

    def expect_description_visible(self):
        expect(self.description_heading).to_be_visible()

    def expect_location_visible(self):
        expect(self.location_text.first).to_be_visible()

    def expect_share_button_visible(self):
        expect(self.share_button).to_be_visible()

    def expect_bookmark_button_visible(self):
        expect(self.bookmark_button).to_be_visible()

    def click_share(self):
        self.share_button.click()

    def click_bookmark(self):
        self.bookmark_button.click()

    def expect_bookmark_toggled(self):
        # Guest flow may open login instead of toggling
        expect(self.bookmark_button).to_have_attribute("aria-pressed", "true")