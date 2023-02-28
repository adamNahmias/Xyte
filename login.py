from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

LOGIN_URL = 'https://partners.xyte.io/auth/sign-in'


class Login:
    user_name: str
    password: str
    driver: webdriver
    cookies: str = 'cookies.pkl'

    def __init__(self, driver: webdriver, user_name: str, password: str):
        self.driver = driver
        self.user_name = user_name
        self.password = password

    def email_label(self) -> WebElement:
        return self.driver.find_element(by=By.NAME, value='email')

    def password_label(self) -> WebElement:
        return self.driver.find_element(by=By.NAME, value='password')

    def sign_in_btn(self) -> WebElement:
        return self.driver.find_element(by=By.XPATH, value='//button[@type="submit"]')

    def login_console(self):
        self.driver.get(LOGIN_URL)
        email = self.email_label()
        password = self.password_label()
        email.send_keys(self.user_name)
        password.send_keys(self.password)
        self.sign_in_btn().click()
