from selenium.webdriver.common.by import By

from tests.selenium.pages.base_page import BasePage
from tests.shared import locators

LINK_XPATH_TPL = "//a[@aria-label='{name}' or contains(normalize-space(), '{name}')]"


class LandingPage(BasePage):
    @property
    def main(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.MAIN)

    @property
    def html(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.HTML)

    @property
    def navigation(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.NAV)

    @property
    def nav_anchor_links(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.NAV_ANCHOR_LINKS)

    @property
    def contact_section(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.CONTACT_SECTION)

    @property
    def meta_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.META_DESCRIPTION)

    @property
    def og_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.OG_TITLE)

    @property
    def og_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.OG_DESCRIPTION)

    @property
    def og_image(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.OG_IMAGE)

    @property
    def portrait(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PORTRAIT_IMG)

    def section(self, section_id):
        return self.driver.find_element(By.CSS_SELECTOR, f"#{section_id}")

    def language_button(self, language):
        # Using the simplified template in locators.py
        selector = locators.LANGUAGE_BUTTON_TPL.format(lang=language.lower())
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def heading(self, name):
        xpath = locators.HEADING_XPATH_TPL.format(name=name)
        return self.driver.find_element(By.XPATH, xpath)

    def link(self, name):
        # Matches the visible text or an explicit aria-label (e.g. "Email").
        selector = LINK_XPATH_TPL.format(name=name)
        return self.driver.find_element(By.XPATH, selector)

    def links(self, name):
        selector = LINK_XPATH_TPL.format(name=name)
        return self.driver.find_elements(By.XPATH, selector)

    def switch_language(self, language):
        self.language_button(language).click()
