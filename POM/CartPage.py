import logging

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from POM.GenericPage import GenericPage


class CartPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_cart(self):
        cart_link = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Cart")]')))
        cart_link.click()

    def get_category_title(self):
        item_name = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                      '(//tr[@class="success"]//*[text()])[1]')))
        return item_name.text

    def click_place_order(self):
        place_order_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Place Order"]')))
        place_order_btn.click()

    def check_place_order_form(self):
        try:
            self.wait.until(ec.visibility_of_all_elements_located
                            ((By.XPATH, '//button[text()="Purchase"]/../..//input')))
        except Exception as e:
            pytest.fail(f'Place Order Form not displayed due to exception: {e}')

    def insert_name(self, name):
        name_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="name"]')))
        name_txt.send_keys(name)

    def insert_country(self, country):
        country_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="country"]')))
        country_txt.send_keys(country)

    def insert_city(self, city):
        city_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="city"]')))
        city_txt.send_keys(city)

    def insert_credit_card(self, card):
        card_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="card"]')))
        card_txt.send_keys(card)

    def insert_month(self, month):
        month_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="month"]')))
        month_txt.send_keys(month)

    def insert_year(self, year):
        year_txt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="year"]')))
        year_txt.send_keys(year)

    def click_purchase_btn(self):
        place_order_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Purchase"]')))
        place_order_btn.click()

    def click_close_form_btn(self):
        place_order_btn = self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//button[text()="Purchase"]/..//button[text()="Close"]')))
        place_order_btn.click()

    def validate_success_purchase_alert(self):
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[contains(@class,"sweet-alert")]')))
        except Exception as e:
            pytest.fail(f'Purchase Order failed due to {e}')

    def get_success_purchase_msg(self):
        success_msg = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                        '//*[contains(@class,"sweet-alert")]//h2')))
        return success_msg.text

    def get_purchase_msg_content(self):
        success_msg_details = self.wait.until(ec.visibility_of_element_located
                                              ((By.XPATH, '//*[contains(@class,"sweet-alert")]//p')))
        return success_msg_details.text

    def get_order_total(self):
        total_txt = self.wait.until(ec.visibility_of_element_located((By.XPATH, '//label[contains(text(),"Total")]')))
        return total_txt.text[7:]

    def click_purchase_ok(self):
        okay_btn = self.wait.until(ec.visibility_of_element_located((By.XPATH, '//button[text()="OK"]')))
        okay_btn.click()

    def click_delete_category(self):
        delete_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Delete")]')))
        delete_btn.click()

    def validate_item_deleted(self):
        try:
            self.wait.until(ec.invisibility_of_element((By.XPATH, '(//tr[@class="success"]//*[text()])[1]')))
            self.wait.until(ec.invisibility_of_element_located((By.XPATH, '//a[contains(text(),"Delete")]')))
        except Exception as e:
            pytest.fail(f'Item still displayed or Place Order button still exists due to {e}')
