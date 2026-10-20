import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage

EXPECTED_TIMER_VALUE = "00:00:00"
TIMER_DELAY_MS = 900


@pytest.mark.unit_4
class TestSessionTimer:
    def test_check_timer_initial_value(self, browser: Browser) -> None:
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        browser.wait_for_delay(TIMER_DELAY_MS)

        actual_timer_value = main_page.get_timer_text()

        assert actual_timer_value == EXPECTED_TIMER_VALUE
