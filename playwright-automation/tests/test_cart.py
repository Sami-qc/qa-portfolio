from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def login(page):
    """Helper: login before each cart test"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")


def test_add_item_to_cart(page: Page):
    """Add item → cart badge should show 1"""
    login(page)
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_cart_badge_updates(page: Page):
    """Add 2 items → cart badge should show 2"""
    login(page)
    inventory = InventoryPage(page)
    buttons = page.locator("[data-test^='add-to-cart']")
    buttons.nth(0).click()
    buttons.nth(1).click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")


def test_remove_item_from_cart(page: Page):
    """Add item then remove it → cart badge should disappear"""
    login(page)
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.remove_first_item()
    expect(page.locator(".shopping_cart_badge")).not_to_be_visible()


def test_cart_page_shows_added_item(page: Page):
    """Add item → go to cart → item should appear in cart"""
    login(page)
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.get_cart_items_count() == 1