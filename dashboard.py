from typing import Optional

from selenium import webdriver

from models import Models

from login import Login


class Devices:
    pass


class Files:
    pass


class Dashboard:
    models: Models
    devices: Devices
    files: Files
    login: Login

    @staticmethod
    def get_dashboard(driver: webdriver):
        models = Models(driver=driver)
        login = Login(driver=driver, user_name="adam1991001@gmail.com", password="Aa5768115123!")
        return Dashboard(models=models, login=login, devices=None, files=None)

    def __init__(self, models: Models, login: Login, devices: Optional[Devices], files: Optional[Files]):
        self.models = models
        self.login = login
        self.files = files
        self.devices = devices
