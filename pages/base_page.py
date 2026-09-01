

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"
        self.endpoint = ""

    def open(self):
        self.driver.get(f"{self.base_url}{self.endpoint}")
