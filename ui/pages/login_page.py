class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-input")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#user-input-btn")
        self.message = page.locator("#message")

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_message(self, expected_text):
        from playwright.sync_api import expect
        expect(self.message).to_have_text(expected_text)