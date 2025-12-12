import pytest
from playwright.sync_api import Playwright, sync_playwright
import json
import os

# ------------------------------
# Load Test Data (JSON)
# ------------------------------
@pytest.fixture(scope="session")
def test_data():
    """
    Loads test data from configs/testdata.json.
    """
    config_path = os.path.join("configs", "testdata.json")
    if os.path.exists(config_path):
        with open(config_path) as f:
            return json.load(f)
    return {}


# ------------------------------
# Browser Fixture
# ------------------------------
def pytest_addoption(parser):
    """
    Custom CLI options for Pytest.
    Allows running tests like:
    pytest --browser chromium --headed
    """
    parser.addoption("--browser", action="store", default="chromium", help="Browser: chromium, firefox, webkit")
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")


@pytest.fixture(scope="session")
def browser_type(pytestconfig):
    """
    Returns selected browser type (chromium, firefox, webkit)
    """
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def headed(pytestconfig):
    """
    Returns True if running in headed mode
    """
    return pytestconfig.getoption("--headed")


@pytest.fixture(scope="session")
def playwright_instance():
    """
    Starts Playwright for the entire session.
    """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_type, headed):
    """
    Browser fixture shared across all tests in the session.
    """
    browser = playwright_instance[browser_type].launch(headless=not headed)
    yield browser
    browser.close()


# ------------------------------
# Page Fixture
# ------------------------------
@pytest.fixture()
def page(browser):
    """
    Creates a new page for each test.
    Ensures clean isolation between tests.
    """
    page = browser.new_page()
    yield page
    page.close()


# ------------------------------
# Screenshot on Failure (Hook)
# ------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Takes a screenshot automatically when a test fails.
    Stores screenshots in: test-results/screenshots/
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshots_dir = "test-results/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            page.screenshot(path=file_path)
            print(f"\n📸 Screenshot saved to: {file_path}")