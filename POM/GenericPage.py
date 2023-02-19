from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GenericPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_accept_alert(self):
        self.wait.until(ec.alert_is_present())
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_text
