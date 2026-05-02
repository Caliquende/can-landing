from playwright.sync_api import expect

from tests.playwright.config import settings
from tests.playwright.data import landing_data
from tests.playwright.pages.landing_page import LandingPage


def test_loads_page_and_renders_main_sections(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    expect(page).to_have_title(landing_data.EXPECTED_TITLE)
    expect(landing_page.main).to_be_visible()

    for section_id in landing_data.MAIN_SECTIONS:
        expect(landing_page.section(section_id)).to_be_visible()


def test_navigation_bar_anchors_point_to_existing_sections(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    link_count = landing_page.nav_anchor_links.count()
    assert link_count > 0

    for index in range(link_count):
        href = landing_page.nav_anchor_links.nth(index).get_attribute("href")

        assert href
        expect(page.locator(href)).to_have_count(1)


def test_switches_language_and_updates_visible_state(page):
    landing_page = LandingPage(page)

    landing_page.goto()
    landing_page.switch_language("TR")

    lang_tr = landing_data.LANGUAGE["turkish"]
    expect(landing_page.html).to_have_attribute("lang", lang_tr["code"])
    expect(landing_page.html).to_have_attribute("data-language", lang_tr["code"])
    expect(landing_page.language_button("TR")).to_have_attribute("aria-pressed", "true")
    expect(landing_page.language_button("EN")).to_have_attribute("aria-pressed", "false")
    expect(page).to_have_title(lang_tr["title"])
    expect(landing_page.meta_description).to_have_attribute(
        "content", lang_tr["description"]
    )
    expect(landing_page.heading(lang_tr["heading"])).to_be_visible()

    landing_page.switch_language("EN")

    lang_en = landing_data.LANGUAGE["english"]
    expect(landing_page.html).to_have_attribute("lang", lang_en["code"])
    expect(landing_page.language_button("EN")).to_have_attribute("aria-pressed", "true")
    expect(page).to_have_title(lang_en["title"])
    expect(landing_page.heading(lang_en["heading"])).to_be_visible()


def test_key_contact_and_external_links_are_configured(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    expect(landing_page.link("Email")).to_have_attribute(
        "href", landing_data.LINKS["email"]
    )
    expect(landing_page.link("LinkedIn").last).to_have_attribute(
        "href", landing_data.LINKS["linkedin"]
    )
    expect(landing_page.link("GitHub")).to_have_attribute(
        "href", landing_data.LINKS["github"]
    )

    for link_name in ["LinkedIn", "GitHub"]:
        link = landing_page.link(link_name).last

        expect(link).to_have_attribute("target", "_blank")
        expect(link).to_have_attribute("rel", "noreferrer")


def test_mobile_viewport_keeps_primary_content_and_controls_visible(page):
    landing_page = LandingPage(page)

    landing_page.set_viewport(settings.MOBILE_VIEWPORT)
    landing_page.goto()

    expect(landing_page.link("Can")).to_be_visible()
    expect(landing_page.language_button("TR")).to_be_visible()
    expect(landing_page.language_button("EN")).to_be_visible()
    expect(landing_page.navigation).to_be_visible()
    expect(landing_page.contact_section).to_be_visible()


def test_metadata_updates_for_both_languages(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    lang_en = landing_data.LANGUAGE["english"]
    expect(landing_page.meta_description).to_have_attribute(
        "content", lang_en["description"]
    )
    expect(landing_page.og_title).to_have_attribute("content", lang_en["title"])
    expect(landing_page.og_description).to_have_attribute(
        "content", lang_en["description"]
    )
    expect(landing_page.og_image).to_have_attribute(
        "content", landing_data.OG_IMAGE
    )

    landing_page.switch_language("TR")

    lang_tr = landing_data.LANGUAGE["turkish"]
    expect(landing_page.meta_description).to_have_attribute(
        "content", lang_tr["description"]
    )
    expect(landing_page.og_title).to_have_attribute("content", lang_tr["title"])
    expect(landing_page.og_description).to_have_attribute(
        "content", lang_tr["description"]
    )


def test_translated_elements_do_not_render_empty_after_language_switches(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    for language in ["TR", "EN"]:
        landing_page.switch_language(language)
        empty_count = page.locator("[data-i18n]").evaluate_all(
            "(elements) => elements.filter((element) => !element.textContent.trim()).length"
        )

        assert empty_count == 0


def test_accessibility_landmarks_and_labels_follow_language(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    skip = page.get_by_role("link", name="Skip to content")
    expect(skip).to_have_attribute("href", "#main")
    expect(page.get_by_role("navigation", name="Primary navigation")).to_be_visible()
    expect(page.get_by_label("Language selection")).to_be_visible()

    landing_page.switch_language("TR")

    skip_tr = page.get_by_role("link", name="İçeriğe geç")
    expect(skip_tr).to_have_attribute("href", "#main")
    expect(page.get_by_role("navigation", name="Birincil navigasyon")).to_be_visible()
    expect(page.get_by_label("Dil seçimi")).to_be_visible()


def test_project_cards_keep_expected_public_project_titles(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    for project_title in landing_data.PROJECT_TITLES:
        expect(page.get_by_text(project_title, exact=True)).to_be_visible()


def test_reference_sections_keep_expected_public_reference_names(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    expect(landing_page.heading("Professional References")).to_be_visible()
    expect(landing_page.heading("Academic Reference")).to_be_visible()

    for reference_name in landing_data.REFERENCE_NAMES:
        expect(page.get_by_text(reference_name, exact=True)).to_be_visible()


def test_static_assets_exist_on_disk(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    for asset_path in ["style.css", "script.js", "favicon.svg"]:
        asset_file = settings.ROOT_DIR / asset_path

        assert asset_file.is_file()
        assert asset_file.stat().st_size > 0


def test_qa_section_details_are_visible(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    expect(landing_page.heading("Quality Assurance & Automated Testing")).to_be_visible()
    expect(page.get_by_text("39 automated tests")).to_be_visible()
    expect(page.get_by_text("Playwright Standalone")).to_be_visible()
    expect(page.get_by_text("Selenium WebDriver")).to_be_visible()

    landing_page.switch_language("TR")

    expect(landing_page.heading("Kalite Güvence ve Otomatik Testler")).to_be_visible()
    expect(page.get_by_text("39 adet otomatik test")).to_be_visible()


def test_external_links_use_expected_blank_target_policy(page):
    landing_page = LandingPage(page)

    landing_page.goto()

    external_links = page.locator("a[target='_blank']")
    link_count = external_links.count()

    assert link_count >= 3

    for index in range(link_count):
        expect(external_links.nth(index)).to_have_attribute("rel", "noreferrer")


def test_tablet_viewport_keeps_primary_content_visible(page):
    landing_page = LandingPage(page)

    landing_page.set_viewport(settings.TABLET_VIEWPORT)
    landing_page.goto()

    expect(landing_page.navigation).to_be_visible()
    expect(landing_page.main).to_be_visible()
    expect(landing_page.contact_section).to_be_visible()
