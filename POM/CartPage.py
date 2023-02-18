import logging

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

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

    def click_delete_category(self):
        delete_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Delete")]')))
        delete_btn.click()

    def validate_item_deleted(self):
        try:
            self.wait.until(ec.invisibility_of_element((By.XPATH, '(//tr[@class="success"]//*[text()])[1]')))
            self.wait.until(ec.invisibility_of_element_located((By.XPATH, '//a[contains(text(),"Delete")]')))
        except Exception as e:
            pytest.fail(f'Item still displayed or Place Order button still exists due to {e}')
