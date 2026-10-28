class BaseComponent:
    def __init__(self, page):
        self.page = page
        self.driver = page.driver