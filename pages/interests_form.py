import pathlib
from typing import Union

from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.checkbox import Checkbox
from framework.ui.elements.elements_list import ElementsList
from framework.ui.elements.file_uploader import FileUploader
from framework.ui.pages.base_page import BasePage
from framework.utils import random_utils


class InterestsForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Button(page, "a[class*='avatar-and-interests']", "Interests form unique element")
        super().__init__(page, unique_element, "Interests Form")
        self._upload_button = FileUploader(page, "a[class*='upload-button']", "Upload button")
        self._next_button = Button(page, page.locator("button[name='button']", has_text="Next"), "Next button")
        self._unselect_all_checkbox = Checkbox(page, "label[for*='unselectall']", "Unselect all checkbox")
        self._interest_checkboxes = ElementsList(page, "label[for*='interest']", "Interests checkboxes", Checkbox)

    def click_random_interests(self, number: int) -> None:
        self._unselect_all_checkbox.click()

        interests = self._interest_checkboxes.get_list_of_elements()
        for _ in range(number):
            interests[random_utils.get_random_int(len(interests))].click()

    def upload_avatar(self, file_path: Union[pathlib.Path, str]) -> None:
        self._upload_button.upload_files_with_chooser(file_path)

    def click_next_button(self) -> None:
        self._next_button.click()
