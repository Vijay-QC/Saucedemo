class CartPage:
    def __init__(self, page):
        self.page = page

    def go_to_checkout(self):
        self.page.click('button[data-test="checkout"]')
