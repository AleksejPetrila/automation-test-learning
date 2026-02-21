import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_login_success(page, demo_server_url):
    page.goto(demo_server_url)

    page.locator("#username").fill("admin")
    page.locator("#password").fill("secret")
    page.locator("#login-btn").click()

    expect(page.locator("#message")).to_have_text("Login successful")


@pytest.mark.ui
@pytest.mark.regression
def test_login_invalid_credentials(page):
    page.goto("http://127.0.0.1:8000")

    page.locator("#username").fill("wrong")
    page.locator("#password").fill("wrong")
    page.locator("#login-btn").click()

    expect(page.locator("#message")).to_have_text("Invalid credentials")