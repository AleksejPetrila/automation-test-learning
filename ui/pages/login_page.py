from playwright.sync_api import expect
#comment

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_test_id("username-input")
        self.password_input = page.get_by_test_id("password-input")
        self.age_input = page.get_by_test_id("age-input")
        self.login_button = page.get_by_test_id("login-button")
        self.message = page.get_by_test_id("message")

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password, age):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.age_input.fill(age)
        self.login_button.click()

    def expect_message(self, expected_text):
        expect(self.message).to_have_text(expected_text)