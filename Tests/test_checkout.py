import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_journey(browser_page):
    inventory = InventoryPage(browser_page)
    cart = CartPage(browser_page)
    checkout = CheckoutPage(browser_page)

    inventory.add_items_to_cart(["sauce-labs-backpack", "sauce-labs-bike-light"])
    inventory.go_to_cart()

    cart.go_to_checkout()
    checkout.fill_checkout_info("John", "Doe", "12345")
    checkout.finish_checkout()

    assert "Thank you for your order!" in checkout.get_confirmation_message()
