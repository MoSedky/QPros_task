import logging

from POM.CartPage import CartPage
from POM.Categories import CategoriesPage
from POM.LoginPage import LoginPage
from POM.RegisterPage import RegisterPage
from constants import MAIN_URL, category_names
from POM.MainPage import MainPage
from Workers.helper_methods import generate_random_string, get_purchase_values, get_current_date


class BlazeWorker:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(MAIN_URL)

    def validate_main_page(self, expected_logo_txt):
        main_page = MainPage(self.driver)
        logo_text = main_page.assert_web_logo()
        assert logo_text.replace(" ", "") == expected_logo_txt.replace(" ", ""), \
            f'Text in Logo different than expected. Current Text: {logo_text}' \
            f'Expected Text: {expected_logo_txt} '
        logging.info('Main Page opens successfully')

    def validate_sign_up(self, expected_alert_txt):
        main_page = MainPage(self.driver)
        main_page.click_register_btn()
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
        main_page = MainPage(self.driver)
        main_page.click_login_btn()
        login_page = LoginPage(self.driver)
        login_page.insert_username(f'username_{rand_txt}')
        login_page.insert_password(f'password_{rand_txt}')
        login_page.click_login_btn_form()
        logged_in_username = login_page.get_logged_in_username()
        assert logged_in_username[8:] == f'username_{rand_txt}', f'Displayed logged in Username is not as expected. ' \
                                                                 f'Current LoggedIn: {logged_in_username[8:]}' \
                                                                 f'Expected Text: username_{rand_txt} '
        logging.info(f'User: username_{rand_txt} logged in successfully')

    def check_select_categories_items(self):
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

    def add_rand_item(self):
        categories_page = CategoriesPage(self.driver)
        item_title = categories_page.click_on_rand_category()
        categories_page.click_add_to_cart()
        success_msg = categories_page.click_accept_alert()
        assert success_msg == 'Product added.', 'Error while attempting to add a product'
        return item_title

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

    def place_order(self, item_name, name, country, city, card_no, month, year):
        cart_page = self.open_cart_page()
        item_title = cart_page.get_category_title()
        assert item_title == item_name, 'Mismatch between displayed item name and item title selected.' \
                                        f'Expected: {item_name} != Current: {item_title}'
        cart_page.click_place_order()
        cart_page.check_place_order_form()
        cart_page.insert_name(name)
        cart_page.insert_country(country)
        cart_page.insert_city(city)
        cart_page.insert_credit_card(card_no)
        cart_page.insert_month(month)
        cart_page.insert_year(year)
        cart_page.click_purchase_btn()
        success_msg = cart_page.get_success_purchase_msg()
        current_total = cart_page.get_order_total()
        current_date = get_current_date()
        assert success_msg == 'Thank you for your purchase!', f'An error in purchase success msg.Current: {success_msg}'
        content_msg = cart_page.get_purchase_msg_content()
        final_msg = content_msg.replace('\n', '')
        id_val, amount_val, card_no_val, name_val, date_val = get_purchase_values(final_msg.strip())
        assert name_val == name, f'Different Name displayed than inserted in purchasing Order. ' \
                                 f'Expected: {name}!= Current: {name_val}'
        assert card_no_val == card_no, f'Different Card Number displayed than inserted in purchasing Order. ' \
                                       f'Expected: {name}!= Current: {name_val}'

        assert current_total == amount_val, f'Different Amount displayed than inserted in purchasing Order. ' \
                                            f'Expected: {current_total}!= Current: {amount_val}'

        assert current_date == date_val, f'Different Date displayed than inserted in purchasing Order. ' \
                                         f'Expected: {current_date}!= Current: {date_val}'

        cart_page.click_purchase_ok()
        logging.info('Order Purchased successfully')
