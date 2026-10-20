import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage


@pytest.mark.unit_4
class TestCookiesPolicy:
    def test_dismiss_cookies_banner(self, browser: Browser) -> None:
        browser.open_url(TEST_APP_URL)

        cookies_form = MainPage(browser.page).cookies_form
        cookies_form.wait_for_page_to_load()
        assert cookies_form.is_page_open()

        cookies_form.click_accept_cookies_button()
        assert not cookies_form.is_page_open()
