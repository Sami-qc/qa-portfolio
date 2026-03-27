from pages.login_page import LoginPage
from utils.test_data import BASE_URL


class LoginFlow:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    def navigate_to_login(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(self.login_page.username_input, username)
        self.page.fill(self.login_page.password_input, password)
        self.page.click(self.login_page.login_button)
