from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    """Valid credentials → should redirect to inventory page"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_password(page: Page):
    """Wrong password → should show error message"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password do not match")


def test_locked_out_user(page: Page):
    """Locked out user → should show locked out error"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Sorry, this user has been locked out")


def test_empty_username(page: Page):
    """Empty username → should show required field error"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "secret_sauce")
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username is required")


def test_empty_password(page: Page):
    """Empty password → should show required field error"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "")
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Password is required")