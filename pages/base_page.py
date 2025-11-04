from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)) is not None
        except:
            return False
