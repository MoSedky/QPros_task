import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=True)
def setup_teardown_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
