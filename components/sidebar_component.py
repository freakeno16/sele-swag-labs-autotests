from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class SidebarComponent(BaseComponent):
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')

    def click_logout_button(self):
        self.page.click(self.LOGOUT_BUTTON)