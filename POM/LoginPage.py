from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from POM.GenericPage import GenericPage


class LoginPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)

    def insert_username(self, username):
        username_txt = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                         '//input[contains(@id,"loginusername")]')))
        username_txt.send_keys(username)

    def insert_password(self, password):
        password_txt = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                         '//input[contains(@id,"loginpassword")]')))
        password_txt.send_keys(password)

    def click_login_btn_form(self):
        login_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Log in")]')))
        login_btn.click()

    def click_close_btn_form(self):
        close_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[contains(text(),'
                                                                '"Log in")]/..//button[text()="Close"]')))
        close_btn.click()

    def get_logged_in_username(self):
        logged_in_username = self.wait.until(ec.visibility_of_element_located((By.XPATH, '//a[@id="nameofuser"]')))
        return logged_in_username.text
