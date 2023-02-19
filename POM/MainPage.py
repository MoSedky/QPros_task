from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from POM.GenericPage import GenericPage


class MainPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)

    def assert_web_logo(self):
        logo = self.wait.until(ec.visibility_of_element_located((By.XPATH, '//a[contains(@href,"index") '
                                                                           'and contains(text(),"PRODUCT")]')))
        return logo.text

    def click_register_btn(self):
        sign_up_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Sign")]')))
        sign_up_btn.click()

    def click_login_btn(self):
        login_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Log in")]')))
        login_btn.click()
