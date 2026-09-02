import os
import dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

dotenv.load_dotenv()

class BasePage:
    BASE_URL = os.getenv("BASE_URL")

    def __init__(self, driver):
        self.driver = driver
        self.endpoint = None
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(f"{self.BASE_URL}{self.endpoint}")

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
