class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill('input[data-test="firstName"]', first_name)
        self.page.fill('input[data-test="lastName"]', last_name)
        self.page.fill('input[data-test="postalCode"]', postal_code)
        self.page.click('input[data-test="continue"]')

    def finish_checkout(self):
        self.page.click('button[data-test="finish"]')

    def get_confirmation_message(self):
        return self.page.locator('.complete-header').inner_text()
