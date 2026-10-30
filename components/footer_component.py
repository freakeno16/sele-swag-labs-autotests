from components.base_component import BaseComponent
from selenium.webdriver.common.by import By

class FooterComponent(BaseComponent):
    COPYRIGHT = (By.CSS_SELECTOR, '[data-test="footer-copy"]')

    def get_copyright_text(self):
        return self.page.get_text(self.COPYRIGHT)

