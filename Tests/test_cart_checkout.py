import pytest
from Workers.BlazeWorker import BlazeWorker
from constants import LOGO_TEXT, SIGNUP_SUCCESS, COUNTRY, CITY, CREDIT_CARD_NO, MONTH, YEAR


class TestUser:

    @pytest.mark.add_delete_rand_item
    def test_case_check_delete_rand_item_from_cart(
            self,
            setup_teardown_driver,
            log,
    ):
        driver = setup_teardown_driver
        blaze_worker = BlazeWorker(driver)
        log.info(f'Check Signup User')
        blaze_worker.validate_main_page(LOGO_TEXT)
        rand_txt = blaze_worker.validate_sign_up(SIGNUP_SUCCESS)
        blaze_worker.validate_login(rand_txt)
        item_title = blaze_worker.add_rand_item()
        blaze_worker.delete_added_item(item_title)

    @pytest.mark.complete_checkout
    def test_case_check_complete_checkout(
            self,
            setup_teardown_driver,
            log,
    ):
        driver = setup_teardown_driver
        blaze_worker = BlazeWorker(driver)
        log.info(f'Check Signup User')
        blaze_worker.validate_main_page(LOGO_TEXT)
        rand_txt = blaze_worker.validate_sign_up(SIGNUP_SUCCESS)
        blaze_worker.validate_login(rand_txt)
        item_title = blaze_worker.add_rand_item()
        blaze_worker.open_cart_page()
        blaze_worker.place_order(item_title, f'username_{rand_txt}', country=COUNTRY,
                                 city=CITY, card_no=CREDIT_CARD_NO, month=str(MONTH), year=str(YEAR))
