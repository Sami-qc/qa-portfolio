from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
