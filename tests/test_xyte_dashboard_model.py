
import pytest as pytest
from selenium.webdriver.remote.webelement import WebElement
from dashboard import Dashboard


class TestXyteDashboardModel:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, dashboard: Dashboard, login_console):
        self.models_list = []
        self.dashboard = dashboard
        self.models = self.dashboard.models
        yield
        self.clean_up()

    def clean_up(self):
        for model_element in self.models_list:
            self.dashboard.models.delete_model(model=model_element)

    def create_model(self, name: str) -> WebElement:
        self.models.add_model(name=name)
        self.models.main_model_btn().click()
        model = self.models.get_model_element_by_name(name=name)
        self.models_list.append(model)
        return model

    def test_dashboard_create_model(self):
        model = self.create_model(name='adam')
        assert model.accessible_name == 'adam'

    def test_create_model_with_same_name(self):
        self.create_model(name="adam")
        self.models.add_model_btn().click()
        assert self.models.contact_us_btn().is_displayed()
        self.models.exit_contact_us_btn().click()

