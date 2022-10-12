"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize(["browser_height", "browser_width"],
                         [(1500, 1800), (800, 600)],
                         ids=["Desktop view", "Mobile view"],
                         )
def test_with_mobile_skip(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 800 and browser_width == 600:
        pytest.skip("Mobile is not tested")
    else:
        browser.open("https://github.com")
        s(by.link_text("Sign in")).click()


@pytest.mark.parametrize(["browser_height", "browser_width"],
                         [(1500, 1800), (800, 600)],
                         ids=["Desktop view", "Mobile view"],
                         )
def test_with_desktop_skip(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser_height == 1500 and browser_width == 1800:
        pytest.skip("Desktop is not tested")
    else:
        browser.open("https://github.com")
        s(".Button-label").click()
        s(by.link_text("Sign in")).click()