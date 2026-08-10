from playwright.sync_api import Page

from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage
from pages.cookies_form import CookiesForm
from pages.help_form import HelpForm
from pages.interests_form import InterestsForm
from pages.personal_details_form import PersonalDetailsForm
from pages.sign_up_form import SignUpForm


class MainPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, ".bagaar-link__image", "Main page unique element")
        super().__init__(page, unique_element, "Main Page")

        self.sign_up_form = SignUpForm(page)
        self.interests_form = InterestsForm(page)
        self.personal_details_form = PersonalDetailsForm(page)
        self.cookies_form = CookiesForm(page)
        self.help_form = HelpForm(page)

        self._timer_label = Label(page, "div.timer--gray", "Timer label")

    def get_timer_text(self) -> str:
        return self._timer_label.get_text()
