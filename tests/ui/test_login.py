import pytest
from playwright.sync_api import expect
from ui.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_login_success(page, demo_server_url):
    login_page = LoginPage(page)
    login_page.open(demo_server_url)
    login_page.login("admin", "secret")
    login_page.expect_message("Login successful")


@pytest.mark.ui
@pytest.mark.regression
def test_login_invalid_credentials(page, demo_server_url):
    login_page = LoginPage(page)
    login_page.open(demo_server_url)
    login_page.login("wrong", "wrong")
    login_page.expect_message("Invalid credentials")