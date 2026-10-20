from playwright.sync_api import Page

from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage
from pages.cookies_form import CookiesForm
from pages.interests_form import InterestsForm
from pages.sign_up_form import SignUpForm


class MainPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, "div.timer--white", "Main page unique element")
        super().__init__(page, unique_element, "Main Page")

        self.sign_up_form = SignUpForm(page)
        self.interests_form = InterestsForm(page)
        self.cookies_form = CookiesForm(page)

        self._timer_label = Label(page, "div.timer--white", "Timer label")

    def get_timer_text(self) -> str:
        return self._timer_label.get_text()
