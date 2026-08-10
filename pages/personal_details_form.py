from playwright.sync_api import Page

from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class PersonalDetailsForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, ".personal-details__form", "Personal Details form unique element")
        super().__init__(page, unique_element, "Personal Details Form")
