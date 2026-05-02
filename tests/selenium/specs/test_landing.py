from tests.selenium.config import settings
from tests.selenium.data import landing_data
from tests.selenium.pages.landing_page import LandingPage


def test_loads_page_and_renders_main_sections(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    assert landing_data.EXPECTED_TITLE.search(driver.title)
    landing_page.assert_visible(landing_page.main)

    for section_id in landing_data.MAIN_SECTIONS:
        landing_page.assert_visible(landing_page.section(section_id))


def test_navigation_bar_anchors_point_to_existing_sections(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    links = landing_page.nav_anchor_links
    assert len(links) > 0

    for link in links:
        href = link.get_dom_attribute("href")

        assert href
        assert len(driver.find_elements("css selector", href)) == 1


def test_switches_language_and_updates_visible_state(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()
    landing_page.switch_language("TR")

    lang_tr = landing_data.LANGUAGE["turkish"]
    assert landing_page.html.get_attribute("lang") == lang_tr["code"]
    assert landing_page.html.get_attribute("data-language") == lang_tr["code"]
    assert landing_page.language_button("TR").get_attribute("aria-pressed") == "true"
    assert landing_page.language_button("EN").get_attribute("aria-pressed") == "false"
    assert lang_tr["title"].search(driver.title)
    assert lang_tr["description"].search(
        landing_page.meta_description.get_attribute("content")
    )
    landing_page.assert_visible(landing_page.heading(lang_tr["heading"]))

    landing_page.switch_language("EN")

    lang_en = landing_data.LANGUAGE["english"]
    assert landing_page.html.get_attribute("lang") == lang_en["code"]
    assert landing_page.language_button("EN").get_attribute("aria-pressed") == "true"
    assert lang_en["title"].search(driver.title)
    landing_page.assert_visible(landing_page.heading(lang_en["heading"]))


def test_key_contact_and_external_links_are_configured(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    assert landing_data.LINKS["email"].search(
        landing_page.link("Email").get_attribute("href")
    )
    assert landing_data.LINKS["linkedin"].search(
        landing_page.links("LinkedIn")[-1].get_attribute("href")
    )
    assert landing_data.LINKS["github"].search(
        landing_page.link("GitHub").get_attribute("href")
    )

    for link_name in ["LinkedIn", "GitHub"]:
        link = landing_page.links(link_name)[-1]

        assert link.get_attribute("target") == "_blank"
        assert link.get_attribute("rel") == "noreferrer"


def test_mobile_viewport_keeps_primary_content_and_controls_visible(driver):
    landing_page = LandingPage(driver)

    landing_page.set_viewport(settings.MOBILE_VIEWPORT)
    landing_page.goto()

    landing_page.assert_visible(landing_page.link("Can"))
    landing_page.assert_visible(landing_page.language_button("TR"))
    landing_page.assert_visible(landing_page.language_button("EN"))
    landing_page.assert_visible(landing_page.navigation)
    landing_page.assert_visible(landing_page.contact_section)


def test_metadata_updates_for_both_languages(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    lang_en = landing_data.LANGUAGE["english"]
    assert lang_en["description"].search(
        landing_page.meta_description.get_attribute("content")
    )
    assert lang_en["title"].search(landing_page.og_title.get_attribute("content"))
    assert lang_en["description"].search(
        landing_page.og_description.get_attribute("content")
    )
    assert landing_data.OG_IMAGE.search(
        landing_page.og_image.get_attribute("content")
    )

    landing_page.switch_language("TR")

    lang_tr = landing_data.LANGUAGE["turkish"]
    assert lang_tr["description"].search(
        landing_page.meta_description.get_attribute("content")
    )
    assert lang_tr["title"].search(landing_page.og_title.get_attribute("content"))
    assert lang_tr["description"].search(
        landing_page.og_description.get_attribute("content")
    )


def test_translated_elements_do_not_render_empty_after_language_switches(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    for language in ["TR", "EN"]:
        landing_page.switch_language(language)
        js = (
            "return Array.from(document.querySelectorAll('[data-i18n]'))"
            ".filter((element) => !element.textContent.trim()).length"
        )
        empty_count = driver.execute_script(js)

        assert empty_count == 0


def test_accessibility_landmarks_and_labels_follow_language(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    skip = driver.find_element("css selector", ".skip-link")
    assert skip.get_dom_attribute("href") == "#main"
    assert landing_page.navigation.get_attribute("aria-label") == "Primary navigation"
    lang_sel = driver.find_element("css selector", "[aria-label='Language selection']")
    assert lang_sel.is_displayed()

    landing_page.switch_language("TR")

    skip_link = driver.find_element("css selector", ".skip-link")
    assert skip_link.get_dom_attribute("href") == "#main"
    text = driver.execute_script("return arguments[0].textContent.trim()", skip_link)
    assert text == "İçeriğe geç"
    assert landing_page.navigation.get_attribute("aria-label") == "Birincil navigasyon"
    dil = driver.find_element("css selector", "[aria-label='Dil seçimi']")
    assert dil.is_displayed()


def test_project_cards_keep_expected_public_project_titles(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    for project_title in landing_data.PROJECT_TITLES:
        el = driver.find_element("xpath", f"//*[normalize-space()='{project_title}']")
        assert el.is_displayed()


def test_reference_sections_keep_expected_public_reference_names(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    assert landing_page.heading("Professional References").is_displayed()
    assert landing_page.heading("Academic Reference").is_displayed()

    for reference_name in landing_data.REFERENCE_NAMES:
        el = driver.find_element(
            "xpath", f"//*[normalize-space()='{reference_name}']"
        )
        assert el.is_displayed()


def test_static_assets_exist_on_disk():
    for asset_path in ["style.css", "script.js", "favicon.svg"]:
        asset_file = settings.ROOT_DIR / asset_path

        assert asset_file.is_file()
        assert asset_file.stat().st_size > 0


def test_external_links_use_expected_blank_target_policy(driver):
    landing_page = LandingPage(driver)

    landing_page.goto()

    external_links = driver.find_elements("css selector", "a[target='_blank']")
    assert len(external_links) >= 3

    for link in external_links:
        assert link.get_attribute("rel") == "noreferrer"


def test_tablet_viewport_keeps_primary_content_visible(driver):
    landing_page = LandingPage(driver)

    landing_page.set_viewport(settings.TABLET_VIEWPORT)
    landing_page.goto()

    landing_page.assert_visible(landing_page.navigation)
    landing_page.assert_visible(landing_page.main)
    landing_page.assert_visible(landing_page.contact_section)
