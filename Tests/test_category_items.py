import pytest
from Workers.BlazeWorker import BlazeWorker
from constants import LOGO_TEXT, SIGNUP_SUCCESS


class TestUser:

    @pytest.mark.categories
    def test_case_check_categories(
            self,
            setup_teardown_driver,
            log,
    ):
        driver = setup_teardown_driver
        blaze_worker = BlazeWorker(driver)
        log.info(f'Checking Category items')
        blaze_worker.validate_main_page(LOGO_TEXT)
        blaze_worker.check_select_categories_items()
