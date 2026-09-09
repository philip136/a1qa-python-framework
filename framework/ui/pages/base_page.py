import logging

from playwright.sync_api import Locator, Page

from framework.ui.constants.elements import WaitForState
from framework.ui.constants.page_events import PageEvent
from framework.ui.constants.timeouts import WaitTimeoutsMs
from framework.ui.elements.base_element import BaseElement

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, page: Page, element: Locator, name: str):
        self._page = page
        self._name = name
        self._unique_element = element

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
        try:
            self.wait_for_page_to_load()
            return True
        except Exception as e:
            logger.debug(f"Failed to open page: {self.name}")
            return False


    def wait_for_page_to_load(self) -> None:
        logger.debug(f"Waiting for page '{self.name}' to load")
        try:
            self._unique_element.wait_for(state=WaitForState.VISIBLE.value, timeout=WaitTimeoutsMs.WAIT_PAGE_LOAD)
            logger.debug(f"Page '{self.name}' loaded")
        except Exception as e:
            logger.error(f"Page '{self.name}' was not loaded: {str(e)}")
            raise
