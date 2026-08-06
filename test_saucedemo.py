import re
from playwright.sync_api import Page, expect 


def test_login_page_loads(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_placeholder("Username")).to_be_visible()


def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()


def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Username and password do not match")).to_be_visible()


def test_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_checkout(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()