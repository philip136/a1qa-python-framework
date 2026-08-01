import re
from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_role("heading", name=re.compile(r"Welcome to the-internet", re.IGNORECASE), level=1), "Main Page Header")
        super().__init__(page, unique_element, "Main Page")

    def _navigation_link(self, text: str) -> Label:
        return Label(self.page, self.page.get_by_role("link", name=text), f"Navigation link: {text}")

    def click_navigation_link(self, navigation_text: str) -> None:
        self._navigation_link(navigation_text).click()
