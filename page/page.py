from page.login_page import LoginPage


class Page:
    @property
    def login(self):
        return LoginPage()
