class InventoryPage:
    def __init__(self, page):
        self.page = page

    def sort_items(self, option_value):
        self.page.select_option('.product_sort_container', option_value)

    def get_item_names(self):
        return self.page.locator('.inventory_item_name').all_inner_texts()

    def get_item_prices(self):
        prices = self.page.locator('.inventory_item_price').all_inner_texts()
        return [float(price.replace('$', '')) for price in prices]

    def add_items_to_cart(self, item_ids):
        for item_id in item_ids:
            self.page.click(f'button[data-test="add-to-cart-{item_id}"]')

    def go_to_cart(self):
        self.page.click('.shopping_cart_link')
