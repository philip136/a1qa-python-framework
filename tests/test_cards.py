from pathlib import Path

import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.utils import random_utils
from pages.main_page import MainPage
from pages.welcome_page import WelcomePage

MIN_PASSWORD_LENGTH = 10
NUMBER_OF_INTERESTS_TO_SELECT = 4


@pytest.mark.unit_4
def test_cards(browser: Browser, file_for_upload: Path):
    browser.open_url(TEST_APP_URL)

    welcome_page = WelcomePage(browser.page)
    welcome_page.wait_for_page_to_load()
    welcome_page.click_here_to_go_link()

    main_page = MainPage(browser.page)
    sign_up_form = main_page.sign_up_form
    sign_up_form.wait_for_page_to_load()
    assert sign_up_form.is_page_open() is True

    email = random_utils.generate_random_alphabetic_string()
    password = random_utils.generate_password(MIN_PASSWORD_LENGTH, email)
    domain = random_utils.generate_random_alphabetic_string()
    domain_postfix = random_utils.get_random_domain()

    sign_up_form.type_password(password)
    sign_up_form.type_email(email)
    sign_up_form.type_domain(domain)
    sign_up_form.select_domain(domain_postfix)
    sign_up_form.click_next_button()

    interests_form = main_page.interests_form
    interests_form.wait_for_page_to_load()
    assert interests_form.is_page_open() is True

    interests_form.click_random_interests(NUMBER_OF_INTERESTS_TO_SELECT)
    interests_form.upload_avatar(file_for_upload)
    interests_form.click_next_button()

    personal_details_form = main_page.personal_details_form
    personal_details_form.wait_for_page_to_load()
    assert personal_details_form.is_page_open() is True
