import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CategoriesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def get_list_categories(self):
        category_items = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH,
                                                                                '//a[text()="CATEGORIES"]/..//a['
                                                                                '@id="itemc"]')))
        return [category_item.text for category_item in category_items]

    def get_items_in_category(self, category_name):
        category_item = self.wait.until(ec.element_to_be_clickable((By.XPATH, f'//a[text()="{category_name}"]')))
        category_item.click()

        category_items = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, '//div[@id="tbodyid"]//div['
                                                                                          '@class="card-block"]')))
        return category_items

    def click_on_rand_category(self):
        category_items = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, '//a[@class="hrefch"]')))
        rand_item = random.choice(category_items)
        rand_item.click()

    def click_add_to_cart(self):
        item = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"cart")]')))
        item.click()

    def check_click_accept_alert(self):
        self.wait.until(ec.alert_is_present())
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_text
