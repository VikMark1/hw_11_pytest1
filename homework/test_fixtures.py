"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_height = 1500
    browser.config.window_width = 1800

@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_height = 800
    browser.config.window_width = 600


def test_github_desktop(desktop_fixture):
    browser.open("https://github.com")
    s(by.link_text("Sign in")).click()


def test_github_mobile(mobile_fixture):
    browser.open("https://github.com")
    s(".Button-label").click()
    s(by.link_text("Sign in")).click()