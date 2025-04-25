class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill('input[data-test="username"]', username)
        self.page.fill('input[data-test="password"]', password)
        self.page.click('input[data-test="login-button"]')
