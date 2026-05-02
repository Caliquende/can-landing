from tests.playwright.pages.base_page import BasePage


class LandingPage(BasePage):
    @property
    def main(self):
        return self.page.locator("main")

    @property
    def html(self):
        return self.page.locator("html")

    @property
    def navigation(self):
        return self.page.get_by_role("navigation")

    @property
    def nav_anchor_links(self):
        return self.page.locator("nav a[href^='#']")

    @property
    def contact_section(self):
        return self.page.locator("#contact")

    @property
    def meta_description(self):
        return self.page.locator('meta[name="description"]')

    @property
    def og_title(self):
        return self.page.locator('meta[property="og:title"]')

    @property
    def og_description(self):
        return self.page.locator('meta[property="og:description"]')

    @property
    def og_image(self):
        return self.page.locator('meta[property="og:image"]')

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
