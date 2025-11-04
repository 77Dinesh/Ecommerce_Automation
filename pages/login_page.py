from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def open_login_page(self, url):
        self.driver.get(url)
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.LOGOUT_LINK)
