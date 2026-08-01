import re
from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

class SecureAreaPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_role("heading", name="Secure Area", level=2), "Secure Area Page Header")
        super().__init__(page, unique_element, "Secure Area Page")
        self._message = Label(page, page.get_by_role("heading", name=re.compile(r"Welcome to the Secure Area", re.IGNORECASE)), "Success message")
        self._logout_button = Button(page, page.get_by_text("Logout", exact=True), "Logout link")

    def get_message_text(self) -> str:
        return self._message.get_text()

    def click_logout_button(self) -> None:
        self._logout_button.click()
