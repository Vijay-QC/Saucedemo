import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=2000)

        # Maximize the browser window by setting the viewport size
        context = browser.new_context()
        page = context.new_page()

        # Get the screen's width and height to set the viewport to the maximum
        # page.set_viewport_size({'width': 1920, 'height': 1080})

        page.goto("https://www.saucedemo.com/")

        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        yield page

        context.close()
        browser.close()
