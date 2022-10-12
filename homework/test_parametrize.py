"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.fixture(params=[(1500, 1800), (800, 600)])
def app(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]


mobile = pytest.mark.parametrize("app", [(800, 600)], indirect=True)
@mobile
def test_mobile_view(app):
    browser.open("https://github.com")
    s(".Button-label").click()
    s(by.link_text("Sign in")).click()

desktop = pytest.mark.parametrize("app", [(1500, 1800)], indirect=True)
@desktop
def test_desktop_view(app):
    browser.open("https://github.com")
    s(by.link_text("Sign in")).click()