from tests.pytest.pages.base_page import BasePage
from tests.shared import locators


class LandingPage(BasePage):
    @property
    def main(self):
        return self.page.locator(locators.MAIN)

    @property
    def html(self):
        return self.page.locator(locators.HTML)

    @property
    def navigation(self):
        return self.page.locator(locators.NAV)

    @property
    def nav_anchor_links(self):
        return self.page.locator(locators.NAV_ANCHOR_LINKS)

    @property
    def contact_section(self):
        return self.page.locator(locators.CONTACT_SECTION)

    @property
    def meta_description(self):
        return self.page.locator(locators.META_DESCRIPTION)

    @property
    def og_title(self):
        return self.page.locator(locators.OG_TITLE)

    @property
    def og_description(self):
        return self.page.locator(locators.OG_DESCRIPTION)

    @property
    def og_image(self):
        return self.page.locator(locators.OG_IMAGE)

    def section(self, section_id):
        return self.page.locator(f"#{section_id}")

    def language_button(self, language):
        return self.page.get_by_role("button", name=language)

    def heading(self, name):
        return self.page.get_by_role("heading", name=name)

    def link(self, name):
        return self.page.get_by_role("link", name=name)

    def switch_language(self, language):
        self.language_button(language).click()
