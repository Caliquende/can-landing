from selenium.webdriver.common.by import By

from tests.selenium.pages.base_page import BasePage


class LandingPage(BasePage):
    @property
    def main(self):
        return self.driver.find_element(By.CSS_SELECTOR, "main")

    @property
    def html(self):
        return self.driver.find_element(By.CSS_SELECTOR, "html")

    @property
    def navigation(self):
        return self.driver.find_element(By.CSS_SELECTOR, "nav")

    @property
    def nav_anchor_links(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "nav a[href^='#']")

    @property
    def contact_section(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#contact")

    @property
    def meta_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'meta[name="description"]')

    @property
    def og_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'meta[property="og:title"]')

    @property
    def og_description(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, 'meta[property="og:description"]'
        )

    @property
    def og_image(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'meta[property="og:image"]')

    def section(self, section_id):
        return self.driver.find_element(By.CSS_SELECTOR, f"#{section_id}")

    def language_button(self, language):
        selector = f'[data-language-button="{language.lower()}"]'
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def heading(self, name):
        xpath = f"//*[self::h1 or self::h2 or self::h3][normalize-space()='{name}']"
        return self.driver.find_element(By.XPATH, xpath)

    def link(self, name):
        return self.driver.find_element(By.LINK_TEXT, name)

    def links(self, name):
        return self.driver.find_elements(By.LINK_TEXT, name)

    def switch_language(self, language):
        self.language_button(language).click()
