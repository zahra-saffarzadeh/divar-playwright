import re

import pytest
from playwright.sync_api import Page, expect

from pages.auth_page import AuthPage
from data.test_data import INVALID_PHONES


def test_open_login_modal(home_with_tehran, page: Page):
    auth_page = AuthPage(page)
    auth_page.open_login()

    auth_page.expect_login_modal_visible()


@pytest.mark.parametrize("phone", INVALID_PHONES)
def test_login_with_invalid_phone(home_with_tehran, page: Page, phone: str):
    auth_page = AuthPage(page)
    auth_page.open_login()
    auth_page.enter_phone(phone)
    auth_page.submit_phone()

    auth_page.expect_invalid_phone_error()


def test_login_with_empty_phone(home_with_tehran, page: Page):
    auth_page = AuthPage(page)
    auth_page.open_login()
    auth_page.submit_phone()

    auth_page.expect_login_modal_visible()


def test_guest_sees_my_divar_button(home_with_tehran, page: Page):
    expect(page.get_by_role("button", name=re.compile(r"دیوار من"))).to_be_visible()


def test_close_login_modal(home_with_tehran, page: Page):
    auth_page = AuthPage(page)
    auth_page.open_login()
    auth_page.expect_login_modal_visible()
    auth_page.close_login_modal()
    expect(auth_page.login_modal).to_be_hidden()