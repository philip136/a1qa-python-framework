from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

PIXELS_SUFFIX = "px"


class HelpForm(BasePage):
    def __init__(self, page: Page):
        self._form = Label(page, ".help-form", "Help form unique element")
        super().__init__(page, self._form, "Help Form")
        self._send_to_bottom_button = Button(page, ".help-form__send-to-bottom-button", "Send to bottom button")

    def click_send_to_bottom_button(self) -> None:
        self._send_to_bottom_button.click()

    def get_height(self) -> float:
        """
        Returns the currently rendered height of the help form in pixels.

        :return: Height of the form in pixels.
        """
        height = self._form.get_css_property("height")
        return float(height.removesuffix(PIXELS_SUFFIX))
