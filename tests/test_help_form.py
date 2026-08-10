import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage
from pages.welcome_page import WelcomePage


@pytest.mark.unit_4
def test_help_form_can_be_collapsed(browser: Browser):
    browser.open_url(TEST_APP_URL)

    welcome_page = WelcomePage(browser.page)
    welcome_page.wait_for_page_to_load()
    welcome_page.click_here_to_go_link()

    help_form = MainPage(browser.page).help_form
    help_form.wait_for_page_to_load()
    assert help_form.is_page_open() is True

    help_form.click_send_to_bottom_button()

    assert help_form.is_page_open() is False
