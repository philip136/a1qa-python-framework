import logging
from typing import Callable, Any, List, Union

from playwright.sync_api import Page

from framework.ui.browser.dialog import DialogHandler
from framework.ui.browser.window import WindowManager
from framework.ui.constants.timeouts import Timeouts
from framework.utils import http_utils

logger = logging.getLogger(__name__)


class Browser:

    def __init__(self, page: Page):
        self._page = page
        self._dialog = DialogHandler(page)
        self._window = WindowManager(self)

    @property
    def page(self) -> Page:
        return self._page

    @page.setter
    def page(self, new_page: Page) -> None:
        """Update the single source of truth for the active page."""
        logger.info("Switching active page context")
        self._page = new_page
        self._dialog = DialogHandler(new_page)

    @property
    def dialog(self) -> DialogHandler:
        return self._dialog

    @property
    def window(self) -> WindowManager:
        return self._window

    def execute_script(self, js_script: str, *args: Any) -> Any:
        """Execute JavaScript code in the browser context."""
        logger.info(f"Executing JS code:\n{js_script}")
        return self.page.evaluate(js_script, *args)

    def get_current_url(self) -> str:
        """Return the current URL of the page."""
        url = self.page.url
        logger.info(f"Current URL: '{url}'")
        return url

    def open_url(self, url: str) -> None:
        """Open the specified URL in the browser."""
        logger.info(f"Open URL: '{url}'")
        self.page.goto(url)

    def press_keys(self, keys: Union[str, List[str]]) -> None:
        """Simulate keyboard key presses."""
        key_list = [keys] if isinstance(keys, str) else keys
        logger.info(f"Pressing key(s): {key_list}")
        for key in key_list:
            self.page.keyboard.press(key)

    def set_basic_authentication(self, user: str, password: str) -> None:
        """
        Set basic HTTP authentication headers for the current browser context.

        :param user: Username for authentication.
        :param password: Password for authentication.
        """
        header = http_utils.generate_basic_auth_header(user, password)
        logger.info("Set basic authentication headers")
        self.page.context.set_extra_http_headers({"Authorization": header})

    def take_screenshot(self, screenshot_name: str, is_wait: bool = False, timer: int = None) -> None:
        """
        Take a screenshot of the current page.

        :param screenshot_name: Filename (without extension) for the screenshot.
        :param is_wait: Whether to wait before taking the screenshot.
        :param timer: Milliseconds to wait before taking the screenshot.
        """
        logger.info(f"Taking screenshot: {screenshot_name}")
        try:
            if is_wait and timer:
                self.wait_for_delay(timer)
            self.page.screenshot(path=f"{screenshot_name}.png")
        except Exception as e:
            logger.error(f"Error taking screenshot: {e}")

    def wait_for_delay(self, timeout: int = Timeouts.DEFAULT_DELAY) -> None:
        """Waits for the given `timeout` in milliseconds."""
        logger.debug(f"Waiting for {timeout}ms")
        self.page.wait_for_timeout(timeout)

    def open_in_new_tab(self, action_callback: Callable[[], Any]) -> Page:
        """
        Executes an action that opens a new browser tab/window,
        waits for it to load, updates the browser's active page, and returns it.

        :param action_callback: A callable that triggers opening the new tab (e.g. clicking a link).
        :return: The newly opened Playwright Page instance.
        """
        logger.info("Opening link in a new tab...")
        with self.page.context.expect_page() as page_info:
            action_callback()
        new_page = page_info.value
        new_page.wait_for_load_state(state="load", timeout=Timeouts.WAIT_PAGE_LOAD)
        self.page = new_page
        logger.info(f"Switched to new tab: '{new_page.url}'")
        return new_page
