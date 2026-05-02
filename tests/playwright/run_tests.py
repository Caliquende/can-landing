import argparse
import importlib
import inspect
import traceback

from playwright.sync_api import sync_playwright

from tests.playwright.config import settings


TEST_MODULE = "tests.playwright.specs.test_landing"

SMOKE_TESTS = {
    "test_loads_page_and_renders_main_sections",
    "test_navigation_bar_anchors_point_to_existing_sections",
    "test_switches_language_and_updates_visible_state",
    "test_key_contact_and_external_links_are_configured",
    "test_mobile_viewport_keeps_primary_content_and_controls_visible",
}


def get_tests(selection):
    module = importlib.import_module(TEST_MODULE)
    tests = [
        (name, function)
        for name, function in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("test_")
    ]

    if selection == "smoke":
        return [(name, function) for name, function in tests if name in SMOKE_TESTS]

    if selection == "regression":
        return tests

    return tests


def run_test(browser, name, function):
    context = browser.new_context(
        base_url=settings.BASE_URL,
        viewport=settings.DESKTOP_VIEWPORT,
    )
    page = context.new_page()

    try:
        function(page)
    finally:
        context.close()


def main():
    parser = argparse.ArgumentParser(description="Run pure Playwright landing page tests.")
    parser.add_argument(
        "--suite",
        choices=["all", "smoke", "regression"],
        default="all",
        help="Select which test group to run.",
    )
    parser.add_argument("--headed", action="store_true", help="Run with a visible browser.")
    args = parser.parse_args()

    tests = get_tests(args.suite)
    failures = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not args.headed)

        try:
            for name, function in tests:
                try:
                    run_test(browser, name, function)
                    print(f"PASS {name}")
                except Exception as error:
                    failures.append((name, error, traceback.format_exc()))
                    print(f"FAIL {name}: {error}")
        finally:
            browser.close()

    if failures:
        print()
        print("Failures:")

        for name, _, stack in failures:
            print(f"\n{name}")
            print(stack)

        return 1

    print()
    print(f"{len(tests)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
