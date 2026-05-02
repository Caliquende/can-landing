import pytest
from playwright.sync_api import sync_playwright

from tests.pytest.config import settings  # noqa: E402
from tests.shared import landing_data


@pytest.fixture(scope="session")
def contact_links():
    """Returns the expected regex patterns for contact links."""
    return landing_data.LINKS


@pytest.fixture(scope="session")
def email_regex(contact_links):
    return contact_links["email"]


@pytest.fixture(scope="session")
def linkedin_regex(contact_links):
    return contact_links["linkedin"]


@pytest.fixture(scope="session")
def github_regex(contact_links):
    return contact_links["github"]


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser tests with a visible browser window.",
    )


@pytest.fixture(scope="session")
def browser(request):
    headed = request.config.getoption("--headed")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        base_url=settings.BASE_URL,
        viewport=settings.DESKTOP_VIEWPORT,
    )
    page = context.new_page()
    yield page
    context.close()
