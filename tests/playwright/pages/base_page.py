from tests.playwright.config import settings


class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(settings.BASE_URL)

    def set_viewport(self, viewport):
        self.page.set_viewport_size(viewport)
