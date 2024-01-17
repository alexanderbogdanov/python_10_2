import locale

import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_config():
    browser.config.window_width = 1600
    browser.config.window_height = 1200

    browser.open('https://google.com')
    yield

    browser.quit()
