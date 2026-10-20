from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class CookiesForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, ".cookies", "Cookies form unique element")
        super().__init__(page, unique_element, "Cookies Form")
        self._accept_cookies_button = Button(
            page,
            "//button[text()='Not really,no']",
            "Accept cookies button",
        )

    def click_accept_cookies_button(self) -> None:
        self._accept_cookies_button.click()
