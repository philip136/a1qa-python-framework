import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage
from pages.welcome_page import WelcomePage


@pytest.mark.unit_4
def test_cookies_form_can_be_hidden(browser: Browser):
    browser.open_url(TEST_APP_URL)

    welcome_page = WelcomePage(browser.page)
    welcome_page.wait_for_page_to_load()
    welcome_page.click_here_to_go_link()

    cookies_form = MainPage(browser.page).cookies_form
    cookies_form.wait_for_page_to_load()
    cookies_form.click_accept_cookies_button()

    assert cookies_form.is_page_open() is False
