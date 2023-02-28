import pytest as pytest
from selenium import webdriver
from dashboard import Dashboard


@pytest.fixture(scope='function')
def dashboard(driver: webdriver) -> Dashboard:
    return Dashboard.get_dashboard(driver)


@pytest.fixture(scope='function')
def login_console(dashboard):
    dashboard.login.login_console()


@pytest.fixture(scope='function')
def driver() -> webdriver:
    return webdriver.Chrome('./chromedriver')
