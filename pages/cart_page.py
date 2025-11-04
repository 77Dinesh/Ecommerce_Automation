from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "(//input[@value='Add to cart'])[1]")
    SHOPPING_CART_LINK = (By.LINK_TEXT, "Shopping cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name a")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)

    def is_product_in_cart(self):
        return self.is_visible(self.PRODUCT_NAME)
