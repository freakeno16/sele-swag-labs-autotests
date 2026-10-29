from components.base_component import BaseComponent
from selenium.webdriver.common.by import By

class FooterComponent(BaseComponent):
    COPYRIGHT = (By.CSS_SELECTOR, '[data-test="footer-copy"]')

    def is_copyright_visible(self):
        return self.page.find(self.COPYRIGHT).is_displayed()
