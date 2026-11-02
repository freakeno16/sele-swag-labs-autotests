import os
import dotenv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from components.footer_component import FooterComponent
from components.header_component import HeaderComponent
from components.sidebar_component import SidebarComponent

dotenv.load_dotenv()

class BasePage:
    BASE_URL = os.getenv("BASE_URL")

    Locator = tuple[str, str]

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.endpoint = None
        self.wait = WebDriverWait(self.driver, 10)

    def open(self) -> None:
        self.driver.get(f"{self.BASE_URL}{self.endpoint}")

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: Locator, text: str) -> None:
        self.find(locator).send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(page=self)

    @property
    def footer(self) -> FooterComponent:
        return FooterComponent(page=self)

    @property
    def sidebar(self) -> SidebarComponent:
        return SidebarComponent(page=self)
