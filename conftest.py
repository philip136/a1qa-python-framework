import json
import logging
from enum import Enum
from pathlib import Path
from typing import Dict

import pytest
from playwright.sync_api import sync_playwright, Playwright

from configs.settings import DEFAULT_CONFIGURATION_FILE, TEST_APP_URL
from framework.logger import logger
from framework.ui.browser.browser import Browser
from framework.ui.constants.timeouts import Timeouts

PROJECT_ROOT_DIR = Path(__file__).parent.resolve()

DEFAULT_VIEWPORT_SIZE = {"width": 1920, "height": 1080}


class SupportedBrowser(Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


def _get_browser(playwright: Playwright, browser_type: SupportedBrowser, headless: bool = False) -> Browser:
    browser_map = {
        SupportedBrowser.FIREFOX: playwright.firefox,
        SupportedBrowser.WEBKIT: playwright.webkit,
        SupportedBrowser.CHROMIUM: playwright.chromium
    }
    browser = browser_map.get(browser_type, playwright.chromium)
    browser_instance = browser.launch(headless=headless)
    context = browser_instance.new_context(viewport=DEFAULT_VIEWPORT_SIZE)
    context.set_default_timeout(Timeouts.WAIT_PAGE_LOAD)

    page = context.new_page()

    custom_browser = Browser(page)
    return custom_browser


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default=SupportedBrowser.CHROMIUM.value,
                     help="Choose a browser: chromium, firefox, webkit")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    parser.addoption("--config", default=DEFAULT_CONFIGURATION_FILE,
                     help="Path to config file relative to the project root directory")


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    logger.setup_logger()
    logging.info("Test logging successfully configured for test execution.")


@pytest.fixture(scope="module")
def browser(request):
    browser_channel = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    with sync_playwright() as playwright:
        browser_instance = _get_browser(playwright, SupportedBrowser(browser_channel), headless)
        yield browser_instance

        # Close the browser after the test is done
        browser_instance.page.close()
        browser_instance.page.context.browser.close()


@pytest.fixture(scope="module")
def set_basic_auth(browser: Browser):
    from framework.utils.env_provider import EnvProvider
    browser.set_basic_authentication(EnvProvider.basic_auth_user(), EnvProvider.basic_auth_password())


@pytest.fixture(scope="session")
def test_config(request) -> Dict[str, str]:
    config_file = request.config.getoption("--config")
    config_path = PROJECT_ROOT_DIR.joinpath(config_file).resolve()
    try:
        with open(config_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception(f"Configuration file not found at: {config_path}")
    return data


@pytest.fixture
def test_file_name(test_config: Dict[str, str]) -> str:
    from framework.utils.config_parser import get_config_value
    return get_config_value(test_config, "download_file_name")


@pytest.fixture
def file_for_upload(test_config: Dict[str, str]) -> Path:
    from framework.utils.config_parser import get_config_value
    file_name = get_config_value(test_config, "file_for_upload")
    resource_dir = get_config_value(test_config, "source_dir", default="tests/resources")
    file_path = PROJECT_ROOT_DIR.joinpath(resource_dir, file_name).resolve()

    if not file_path.is_file():
        raise FileNotFoundError(f"File for upload not found: {file_path}")

    return file_path


@pytest.fixture
def download_dir(test_config: Dict[str, str]) -> Path:
    from framework.utils.config_parser import get_config_value
    download_dir = get_config_value(test_config, "download_dir", default="downloads")
    return PROJECT_ROOT_DIR.joinpath(download_dir).resolve()


@pytest.fixture
def cleanup_download_dir(download_dir: Path) -> Path:
    import shutil
    shutil.rmtree(download_dir, ignore_errors=True)
    try:
        yield download_dir
    finally:
        shutil.rmtree(download_dir, ignore_errors=True)
