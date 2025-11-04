import pytest
from utilities.driver_setup import get_driver
from utilities.config_reader import ReadConfig
from pages.search_page import SearchPage
from pages.cart_page import CartPage

@pytest.fixture()
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_add_to_cart(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())

    search_page = SearchPage(driver)
    search_page.search_product("Laptop")

    cart_page = CartPage(driver)
    cart_page.add_product_to_cart()
    cart_page.open_cart()

    assert cart_page.is_product_in_cart()
