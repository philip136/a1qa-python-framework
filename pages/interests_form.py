from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class InterestsForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Button(page, "a[class*='avatar-and-interests']", "Interests form unique element")
        super().__init__(page, unique_element, "Interests Form")
        self._page_indicator = Label(page, "div.page-indicator", "Page indicator")

    def get_page_indicator_text(self) -> str:
        return self._page_indicator.get_text()
