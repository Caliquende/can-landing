import argparse
import importlib
import inspect
import os
import sys
import tempfile
import traceback
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

# Some environments ship a third-party `tests` module/package. Ensure we load ours.
loaded_tests = sys.modules.get("tests")
if loaded_tests and getattr(loaded_tests, "__file__", ""):
    if str(ROOT_DIR) not in str(loaded_tests.__file__):
        del sys.modules["tests"]

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
    cache_root = Path(tempfile.gettempdir()) / "selenium"
    cache_root.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("SELENIUM_MANAGER_CACHE", str(cache_root))
    os.environ.setdefault("SE_CACHE_PATH", str(cache_root))
    os.environ.setdefault("XDG_CACHE_HOME", str(cache_root))

    options = Options()

    if not headed:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=0")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        profile_dir = Path(tempfile.gettempdir()) / "selenium-chrome-profile"
        profile_dir.mkdir(parents=True, exist_ok=True)
        options.add_argument(f"--user-data-dir={profile_dir}")

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
