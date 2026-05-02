# Shared CSS Selectors
MAIN = "main"
HTML = "html"
NAV = "nav"
NAV_ANCHOR_LINKS = "nav a[href^='#']"
CONTACT_SECTION = "#contact"
META_DESCRIPTION = 'meta[name="description"]'
OG_TITLE = 'meta[property="og:title"]'
OG_DESCRIPTION = 'meta[property="og:description"]'
OG_IMAGE = 'meta[property="og:image"]'

# Templates
LANGUAGE_BUTTON_TPL = "button[data-language-button='{lang}']"
HEADING_XPATH_TPL = "//*[self::h1 or self::h2][contains(text(), '{name}')]"
