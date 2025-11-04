from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Search']")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-title a")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_first_product_name(self):
        return self.get_element_text(self.PRODUCT_LINK)
