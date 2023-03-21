from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

MODEL_URL = 'https://partners.xyte.io/models'


class Models:
    driver: webdriver

    def __init__(self, driver: webdriver):
        driver.get(MODEL_URL)
        self.driver = driver

    def add_model_btn(self) -> WebElement:
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(By.XPATH, value='//span[text()="Add Model"]'))

    def display_name(self) -> WebElement:
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(by=By.NAME, value='name'))

    def save_btn(self) -> WebElement:
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(by=By.XPATH, value='//span[text()="Save"]'))

    def get_model_element_by_name(self, name: str) -> WebElement:
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(by=By.LINK_TEXT, value=name))

    def main_model_btn(self) -> WebElement:
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(by=By.LINK_TEXT, value='Models'))

    def delete_model_btn(self):
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(By.XPATH, value='//span[text()="Delete"]'))

    def confirm_btn(self):
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(By.XPATH, value='//span[text()="Confirm"]'))

    def contact_us_btn(self):
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(By.XPATH, value='//span[text()="Contact Us"]'))

    def exit_contact_us_btn(self):
        return WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.find_element(By.XPATH, value='//button[@class="mantine-UnstyledButton-root mantine-ActionIcon-root mantine-1xsn816"]'))

    def add_model(self, name: str):
        self.add_model_btn().click()
        self.display_name().send_keys(name)
        self.save_btn().click()

    def delete_model(self, model: WebElement):
        model.click()
        self.delete_model_btn().click()
        self.confirm_btn().click()

