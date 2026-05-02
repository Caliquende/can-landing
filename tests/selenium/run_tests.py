import argparse
import importlib
import inspect
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.selenium.config import settings


TEST_MODULE = "tests.selenium.specs.test_landing"

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


def create_driver(headed):
    options = Options()

    if not headed:
        options.add_argument("--headless=new")

    width = settings.DESKTOP_VIEWPORT["width"]
    height = settings.DESKTOP_VIEWPORT["height"]
    options.add_argument(f"--window-size={width},{height}")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


def run_test(driver, name, function):
    signature = inspect.signature(function)

    if "driver" not in signature.parameters:
        function()
        return

    function(driver)


def main():
    parser = argparse.ArgumentParser(description="Run pure Selenium landing page tests.")
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

    driver = create_driver(args.headed)

    try:
        for name, function in tests:
            try:
                run_test(driver, name, function)
                print(f"PASS {name}")
            except Exception as error:
                failures.append((name, error, traceback.format_exc()))
                print(f"FAIL {name}: {error}")
    finally:
        driver.quit()

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
