import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.inventory_page import InventoryPage

def test_sorting_z_to_a(browser_page):
    inventory = InventoryPage(browser_page)
    inventory.sort_items("za")
    names = inventory.get_item_names()
    assert names == sorted(names, reverse=True), "Names not sorted Z-A"

def test_sort_price_high_to_low(browser_page):
    inventory = InventoryPage(browser_page)
    inventory.sort_items("hilo")
    prices = inventory.get_item_prices()
    assert prices == sorted(prices, reverse=True), "Prices not sorted High to Low"
