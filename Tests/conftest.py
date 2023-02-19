import logging
import pytest
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=True)
def setup_teardown_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                              options=chrome_options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
