import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage
from pages.welcome_page import WelcomePage

EXPECTED_TIMER_VALUE = "00:00:00"


@pytest.mark.unit_4
def test_timer_initial_value(browser: Browser):
    browser.open_url(TEST_APP_URL)

    welcome_page = WelcomePage(browser.page)
    welcome_page.wait_for_page_to_load()
    welcome_page.click_here_to_go_link()

    main_page = MainPage(browser.page)
    main_page.wait_for_page_to_load()

    assert main_page.get_timer_text() == EXPECTED_TIMER_VALUE
