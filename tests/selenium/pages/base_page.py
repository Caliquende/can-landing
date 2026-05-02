from tests.selenium.config import settings


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def goto(self):
        self.driver.get(settings.BASE_URL)

    def set_viewport(self, viewport):
        self.driver.set_window_size(viewport["width"], viewport["height"])

    @staticmethod
    def assert_visible(element):
        assert element.is_displayed()
