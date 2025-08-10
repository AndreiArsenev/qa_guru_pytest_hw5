import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.timeout = 60
    yield
    browser.quit()