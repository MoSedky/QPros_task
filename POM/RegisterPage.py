from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from POM.GenericPage import GenericPage


class RegisterPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)

    def insert_username(self, username):
        username_txt = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                         '//input[contains(@id,"sign-user")]')))
        username_txt.send_keys(username)

    def insert_password(self, password):
        password_txt = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                         '//input[contains(@id,"sign-pass")]')))
        password_txt.send_keys(password)

    def click_signup_btn_form(self):
        sign_up_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH,
                                                                  '//button[contains(text(),"Sign")]')))
        sign_up_btn.click()

    # def click_accept_alert(self):
    #     self.wait.until(ec.alert_is_present())
    #     alert_text = self.driver.switch_to.alert.text
    #     self.driver.switch_to.alert.accept()
    #     return alert_text

    def click_close_btn_form(self):
        close_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH,
                                                                '//button[contains(text(),'
                                                                '"Sign")]/..//button[text()="Close"]')))
        close_btn.click()
