import pytest
from utilities.driver_setup import get_driver
from utilities.config_reader import ReadConfig
from pages.login_page import LoginPage

@pytest.fixture()
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_valid(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page(ReadConfig.getApplicationURL())
    login_page.login(ReadConfig.getEmail(), ReadConfig.getPassword())
    assert login_page.is_login_successful()
