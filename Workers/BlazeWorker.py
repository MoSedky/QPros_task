import logging

from POM.CartPage import CartPage
from POM.Categories import CategoriesPage
from POM.LoginPage import LoginPage
from POM.RegisterPage import RegisterPage
from constants import MAIN_URL, category_names
from POM.MainPage import MainPage
from helper_methods import generate_random_string


class BlazeWorker:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(MAIN_URL)

    def validate_main_page(self, expected_logo_txt):
        main_page = MainPage(self.driver)
        logo_text = main_page.assert_web_logo()
        assert logo_text == expected_logo_txt, f'Text in Logo different that expected. Current Text: {logo_text}' \
                                               f'Expected Text: {expected_logo_txt} '
        logging.info('Main Page opens successfully')

    def validate_sign_up(self, expected_alert_txt):
        register_page = RegisterPage(self.driver)
        random_text = generate_random_string()
        register_page.insert_username(f'username_{random_text}')
        register_page.insert_password(f'password_{random_text}')
        register_page.click_signup_btn_form()
        alert_txt = register_page.click_accept_alert()
        assert alert_txt == expected_alert_txt, f'Text in Alert is different than expected. Current Text: {alert_txt}' \
                                                f'Expected Text: {expected_alert_txt} '
        logging.info(f'User: username_{random_text} registered successfully')
        return random_text

    def validate_login(self, rand_txt):
        login_page = LoginPage(self.driver)
        login_page.insert_username(f'username_{rand_txt}')
        login_page.insert_password(f'password_{rand_txt}')
        login_page.click_login_btn_form()
        logged_in_username = login_page.get_logged_in_username()
        assert logged_in_username == f'username_{rand_txt}', f'Displayed logged in Username is not as expected. ' \
                                                             f'Current LoggedIn: {logged_in_username}' \
                                                             f'Expected Text: username_{rand_txt} '
        logging.info(f'User: username_{rand_txt} logged in successfully')

    def check_categories_items(self):
        categories_page = CategoriesPage(self.driver)
        list_categories = categories_page.get_list_categories()
        list_categories.sort()
        category_names.sort()
        assert list_categories == category_names, f'List of Categories is not as expected. Current {list_categories}' \
                                                  f'!= Expected {category_names}'

        for category in category_names:
            items_in_category = categories_page.get_items_in_category(category_name=category)
            assert len(items_in_category) > 1, f'Item list in category: {category} is empty'

        logging.info(f'All Categories have items as expected')
        logging.info('Now adding an item randomly to be added to the cart')
        categories_page.click_on_rand_category()
        categories_page.click_add_to_cart()
        success_msg = categories_page.check_click_accept_alert()
        assert success_msg == 'Product added.', 'Error while attempting to add a product'

    def open_cart_page(self):
        cart_page = CartPage(self.driver)
        cart_page.click_on_cart()
        return cart_page

    def delete_added_item(self, item_name):
        cart_page = self.open_cart_page()
        item_title = cart_page.get_category_title()
        assert item_title == item_name, 'Mismatch between displayed item name and item title selected.' \
                                        f'Expected: {item_name} != Current: {item_title}'
        cart_page.click_delete_category()
        cart_page.validate_item_deleted()
