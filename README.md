# can-landing

Bilingual static personal landing page for Hamdi Can Ernalbantogullari's QA Engineer, Test Automation Engineer, and SDET profile.

## Overview

This repository contains a deployment-ready single-page site built with plain HTML, CSS, and JavaScript. It includes English and Turkish content, profile summary sections, QA/SDET skill highlights, project cards, contact actions, and basic SEO/Open Graph metadata.

The site itself has no build step and no runtime package manager dependency. Automated browser tests use Python dependencies under `tests/`.

## Repository Structure

```text
.
├── index.html
├── style.css
├── script.js
├── favicon.svg
├── SECURITY.md
├── wrangler.jsonc
├── pyproject.toml
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
└── tests/
    ├── shared/
    │   └── landing_data.py       # Single source of truth for test data
    ├── playwright/               # Standalone Playwright suite
    │   ├── config/settings.py
    │   ├── data/landing_data.py
    │   ├── pages/
    │   │   ├── base_page.py
    │   │   └── landing_page.py
    │   ├── specs/test_landing.py
    │   ├── requirements.txt
    │   └── run_tests.py
    ├── pytest/                   # Pytest-based Playwright suite
    │   ├── config/settings.py
    │   ├── data/landing_data.py
    │   ├── pages/
    │   │   ├── base_page.py
    │   │   └── landing_page.py
    │   ├── specs/test_landing.py
    │   ├── conftest.py
    │   ├── pytest.ini
    │   └── requirements.txt
    └── selenium/                 # Standalone Selenium suite
        ├── config/settings.py
        ├── data/landing_data.py
        ├── pages/
        │   ├── base_page.py
        │   └── landing_page.py
        ├── specs/test_landing.py
        ├── requirements.txt
        └── run_tests.py
```

## Local Preview

Open `index.html` directly in a browser.

## Deployment

The repository is suitable for GitHub Pages, Netlify, Vercel, Cloudflare Pages, or any static hosting provider.

Before publishing, verify both language modes and all contact links.

## Validation

Check the page after every content or style update:

- Open the page on desktop and mobile widths.
- Switch between English and Turkish.
- Verify contact links and language-specific content.
- Confirm metadata in `index.html` still matches the current public profile.

## Testing

This repository uses three separate Python browser test suites with mirrored smoke and regression coverage:

- `tests/pytest`: pytest-run Playwright browser suite.
- `tests/playwright`: pure Playwright Python runner.
- `tests/selenium`: pure Selenium Python runner.

The browser suites open the checked-out `index.html` directly through their suite-level settings files. No local server is required.

Install dependencies:

```powershell
python -m pip install -r tests/pytest/requirements.txt
python -m pip install -r tests/playwright/requirements.txt
python -m pip install -r tests/selenium/requirements.txt
python -m playwright install chromium
```

Selenium tests require a local Chrome installation. Selenium Manager handles driver resolution in supported environments.

Run smoke tests:

```powershell
# Pytest (PYTHONPATH is handled by pyproject.toml)
python -m pytest tests/pytest -c tests/pytest/pytest.ini -m smoke

# Playwright Standalone ($env:PYTHONPATH="." for PowerShell, PYTHONPATH=. for Bash)
$env:PYTHONPATH="."; python tests/playwright/run_tests.py --suite smoke

# Selenium Standalone
$env:PYTHONPATH="."; python tests/selenium/run_tests.py --suite smoke
```

Run regression tests:

```powershell
# Pytest
python -m pytest tests/pytest -c tests/pytest/pytest.ini -m regression

# Playwright Standalone
$env:PYTHONPATH="."; python tests/playwright/run_tests.py --suite regression

# Selenium Standalone
$env:PYTHONPATH="."; python tests/selenium/run_tests.py --suite regression
```

Run the full test suite:

```powershell
# Pytest
python -m pytest tests/pytest -c tests/pytest/pytest.ini

# Playwright Standalone
$env:PYTHONPATH="."; python tests/playwright/run_tests.py

# Selenium Standalone
$env:PYTHONPATH="."; python tests/selenium/run_tests.py
```

Optional headed/browser UI runs:

```powershell
# Pytest
python -m pytest tests/pytest -c tests/pytest/pytest.ini --headed

# Playwright Standalone
$env:PYTHONPATH="."; python tests/playwright/run_tests.py --headed

# Selenium Standalone
$env:PYTHONPATH="."; python tests/selenium/run_tests.py --headed
```

CI runs smoke tests for all three suites against the checked-out files. Full regression runs are available through the commands above and are not run by default in CI.

Covered by automated tests:

- Page load and main section visibility.
- Navigation bar anchor links target existing sections.
- English/Turkish language switching updates visible state, document language, title, and meta description.
- Key contact links for email, LinkedIn, and GitHub.
- Mobile and Tablet viewport smoke checks.
- Regression checks for metadata (including og:image), translated text completeness, accessibility labels, project/reference visibility, static asset presence (css, js, favicon), and external link policy.

Not covered by automated tests:

- Pixel-perfect CSS/layout validation.
- Third-party website availability.
- Full CV/content parity checks.
- Copy-to-clipboard behavior, because the current site does not implement that feature.
- Full accessibility audits beyond basic landmark/control smoke checks.

## Security

This repository follows standard security practices for static sites:
- **Dependabot:** Keeps GitHub Actions and Python test dependencies updated.
- **Security Policy:** Outlined in [SECURITY.md](./SECURITY.md).
- **Blocking CI Scanning:** CI fails on common hardcoded secret and unsafe JavaScript patterns.
