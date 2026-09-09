import pytest
from typing import Dict
from framework.ui.browser.browser import Browser
from framework.utils.env_provider import EnvProvider
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from configs.settings import TEST_APP_URL

@pytest.mark.demo
def test_demo_for_successful_login(browser: Browser, test_config: Dict[str, str]):
    browser.open_url(TEST_APP_URL)
    
    test_data = test_config
    
    main_page = MainPage(browser.page)
    main_page.click_navigation_link("Form Authentication")

    login_page = LoginPage(browser.page)
    login_page.wait_for_page_to_load()
    assert login_page.is_page_open() is True
    
    login_page.type_username(EnvProvider.test_user())
    login_page.type_password(EnvProvider.test_password())
    login_page.click_login_button()

    secure_area_page = SecureAreaPage(browser.page)
    secure_area_page.wait_for_page_to_load()
    assert secure_area_page.is_page_open() is True
    
    message = secure_area_page.get_message_text()
    assert message == test_data.get("login_success_message")

    secure_area_page.click_logout_button()
    login_page.wait_for_page_to_load()
    assert login_page.is_page_open() is True
