import logging

from playwright.sync_api import Locator, Page

from framework.ui.constants.elements import WaitForState
from framework.ui.constants.timeouts import Timeouts
from framework.ui.elements.base_element import BaseElement

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, page: Page, unique_element: BaseElement, name: str):
        if not isinstance(unique_element, BaseElement):
            raise TypeError("unique_element must be an instance of BaseElement")
        self._page = page
        self._name = name
        self._unique_element = unique_element

    @property
    def name(self) -> str:
        return self._name

    @property
    def page(self) -> Page:
        return self._page

    @page.setter
    def page(self, value: Page) -> None:
        self._page = value

    def get_title(self) -> str:
        return self.page.title()

    def is_page_open(self) -> bool:
        """Non-blocking visibility snapshot (matches JS isPageOpened)."""
        return self._unique_element.state.is_displayed()


    def wait_for_page_to_load(self) -> None:
        """Wait for the page's unique element to become visible."""
        logger.debug(f"Waiting for page '{self.name}' to load")
        try:
            self._unique_element.state.wait_for_displayed(timeout=Timeouts.WAIT_PAGE_LOAD)
            logger.debug(f"Page '{self.name}' loaded")
        except Exception as e:
            logger.error(f"Page '{self.name}' was not loaded: {str(e)}")
            raise
