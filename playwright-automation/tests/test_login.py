from playwright.sync_api import Page, expect

from flows.login_flow import LoginFlow
from utils.test_data import (
    EMPTY_VALUE,
    INVALID_PASSWORD,
    LOCKED_OUT_USER,
    STANDARD_USER,
    VALID_PASSWORD,
)


def test_valid_login(page: Page):
    """Valid credentials should redirect to inventory page"""
    login_flow = LoginFlow(page)
    login_flow.navigate_to_login()
    login_flow.login(STANDARD_USER, VALID_PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_password(page: Page):
    """Wrong password should show error message"""
    login_flow = LoginFlow(page)
    login_flow.navigate_to_login()
    login_flow.login(STANDARD_USER, INVALID_PASSWORD)
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password do not match")


def test_locked_out_user(page: Page):
    """Locked out user should show locked out error"""
    login_flow = LoginFlow(page)
    login_flow.navigate_to_login()
    login_flow.login(LOCKED_OUT_USER, VALID_PASSWORD)
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Sorry, this user has been locked out")


def test_empty_username(page: Page):
    """Empty username should show required field error"""
    login_flow = LoginFlow(page)
    login_flow.navigate_to_login()
    login_flow.login(EMPTY_VALUE, VALID_PASSWORD)
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username is required")


def test_empty_password(page: Page):
    """Empty password should show required field error"""
    login_flow = LoginFlow(page)
    login_flow.navigate_to_login()
    login_flow.login(STANDARD_USER, EMPTY_VALUE)
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Password is required")
