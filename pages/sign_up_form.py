from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.input import Input
from framework.ui.pages.base_page import BasePage

DOMAIN_ITEM_LOCATOR_TEMPLATE = "//div[contains(@class,'dropdown__list-item') and normalize-space(text())='{domain}']"


class SignUpForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Input(page, page.get_by_placeholder("Choose Password"), "Sign Up form unique element")
        super().__init__(page, unique_element, "Sign Up Form")
        self._password_input = Input(page, page.get_by_placeholder("Choose Password"), "Password input")
        self._email_input = Input(page, page.get_by_placeholder("email"), "Email input")
        self._domain_input = Input(page, page.get_by_placeholder("Domain"), "Domain input")
        self._domain_dropdown_opener = Button(page, "div[class*='opener']", "Domain dropdown opener")
        self._next_button = Button(page, page.locator("a.button--secondary", has_text="Next"), "Next button")

    def type_password(self, password: str) -> None:
        self._password_input.type_text_with_clear(password)

    def type_email(self, email: str) -> None:
        self._email_input.type_text_with_clear(email)

    def type_domain(self, domain: str) -> None:
        self._domain_input.type_text_with_clear(domain)

    def select_domain(self, domain: str) -> None:
        self._domain_dropdown_opener.click()
        self._domain_dropdown_item(domain).click()

    def click_next_button(self) -> None:
        self._next_button.click()

    def _domain_dropdown_item(self, domain: str) -> Button:
        return Button(self.page, DOMAIN_ITEM_LOCATOR_TEMPLATE.format(domain=domain), f"'{domain}' domain dropdown item")
