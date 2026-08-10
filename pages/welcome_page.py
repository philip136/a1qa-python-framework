from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage


class WelcomePage(BasePage):
    def __init__(self, page: Page):
        unique_element = Button(page, ".start__button", "Welcome page unique element")
        super().__init__(page, unique_element, "Welcome Page")
        self._click_here_to_go_link = Button(page, page.get_by_role("link", name="HERE"), "Click HERE to GO link")

    def click_here_to_go_link(self) -> None:
        self._click_here_to_go_link.click()
