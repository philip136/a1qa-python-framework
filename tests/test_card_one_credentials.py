from dataclasses import replace

import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from models.registration_creds import RegistrationCreds
from pages.main_page import MainPage
from pages.sign_up_form import SignUpForm

FIRST_CARD_INDICATOR = "1 / 4"
SECOND_CARD_INDICATOR = "2 / 4"


@pytest.mark.unit_4
class TestCardOneCredentials:
    def test_check_password_policy_compliance(
        self,
        browser: Browser,
        first_card_creds: RegistrationCreds,
    ) -> None:
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        sign_up_form = main_page.sign_up_form
        interests_form = main_page.interests_form

        sign_up_form.wait_for_page_to_load()
        assert sign_up_form.get_page_indicator_text() == FIRST_CARD_INDICATOR

        self._fill_credentials(sign_up_form, first_card_creds)
        sign_up_form.click_next_button()

        assert interests_form.get_page_indicator_text() == SECOND_CARD_INDICATOR

    def test_check_email_domain_extensions(
        self,
        browser: Browser,
        second_card_creds: RegistrationCreds,
        domains: tuple[str, ...],
    ) -> None:
        for domain in domains:
            browser.open_url(TEST_APP_URL)

            main_page = MainPage(browser.page)
            sign_up_form = main_page.sign_up_form
            interests_form = main_page.interests_form

            sign_up_form.wait_for_page_to_load()
            assert sign_up_form.get_page_indicator_text() == FIRST_CARD_INDICATOR

            creds = replace(second_card_creds, domain_extension=domain)
            self._fill_credentials(sign_up_form, creds)
            sign_up_form.click_next_button()

            interests_form.wait_for_page_to_load()
            assert interests_form.get_page_indicator_text() == SECOND_CARD_INDICATOR

    @staticmethod
    def _fill_credentials(sign_up_form: SignUpForm, creds: RegistrationCreds) -> None:
        sign_up_form.type_password(creds.password)
        sign_up_form.type_email(creds.email_name)
        sign_up_form.type_domain(creds.email_domain)
        sign_up_form.select_domain(creds.domain_extension)
        sign_up_form.accept_terms_conditions()
