import pytest
from utilities.driver_setup import get_driver
from utilities.config_reader import ReadConfig
from pages.search_page import SearchPage

@pytest.fixture()
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_product(setup):
    driver = setup
    search_page = SearchPage(driver)
    driver.get(ReadConfig.getApplicationURL())
    search_page.search_product("Laptop")
    product_name = search_page.get_first_product_name()
    assert product_name and len(product_name) > 0
