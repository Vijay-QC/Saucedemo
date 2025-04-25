import os

def test_visual_inventory_page(browser_page):
    browser_page.wait_for_timeout(1000)
    os.makedirs("screenshots", exist_ok=True)
    browser_page.screenshot(path="screenshots/inventory.png", full_page=True)
    assert os.path.exists("screenshots/inventory.png")
