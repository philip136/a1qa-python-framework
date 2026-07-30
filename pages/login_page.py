from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.elements.input import Input
from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_role("heading", name="Login Page"), "Login Page Header")
        super().__init__(page, unique_element, "Login Page")
        self._username_input = Input(page, page.get_by_label("Username"), "Username input")
        self._password_input = Input(page, page.get_by_label("Password"), "Password input")
        self._login_button = Button(page, page.get_by_role("button", name="Login"), "Login button")

    def type_username(self, username: str) -> None:
        self._username_input.type_text(username)

    def type_password(self, password: str) -> None:
        self._password_input.type_secret(password)

    def click_login_button(self) -> None:
        self._login_button.click()
