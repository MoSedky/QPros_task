import pytest
from Workers.BlazeWorker import BlazeWorker
from constants import LOGO_TEXT, SIGNUP_SUCCESS


class TestUser:

    @pytest.mark.signup_login
    def test_case_check_signup_login_scenario(
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
