# can-landing

Bilingual static personal landing page for Hamdi Can Ernalbantoğullari's QA Engineer, Test Automation Engineer, and SDET profile.

## Overview

This repository contains a deployment-ready single-page site built with plain HTML, CSS, and JavaScript. It opens in English and switches to Turkish with the TR/EN control in the header. The page covers profile summary, experience, references note, skill highlights, project cards, contact actions, and SEO/Open Graph metadata.

The site itself has no build step and no runtime package manager dependency. Automated browser tests use Python dependencies under `tests/`. The landing page also features a dedicated section that highlights its own automated test coverage and architecture.

## Repository Structure

```text
.
├── index.html
├── style.css
├── script.js
├── favicon.svg
├── assets/
│   ├── can.png
│   └── cv.pdf
├── SECURITY.md
├── wrangler.jsonc
├── pyproject.toml
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
└── tests/
    ├── pytest/
    ├── playwright/
    ├── selenium/
    └── shared/
```

## Content Sources

- `index.html` holds the English copy and the `data-i18n`, `data-i18n-aria`, and `data-i18n-content` hooks.
- `script.js` holds the Turkish dictionary and applies the active language to text, ARIA labels, metadata, and the `lang`/`data-language` attributes.
- `assets/can.png` is the portrait and the Open Graph image; `assets/cv.pdf` is the downloadable CV.

## Automated Tests

The page is verified by three independent suites: Pytest, Playwright, and Selenium. They check loading, section visibility, navigation anchors, both languages, metadata, accessibility landmarks, contact links, the CV download, the portrait, and the responsive layouts.

Run them with the `PYTHONPATH` set to the repository root:

```bash
PYTHONPATH=. pytest tests/pytest
PYTHONPATH=. pytest tests/playwright
PYTHONPATH=. pytest tests/selenium
```

## Deployment

The site is served as static assets by Cloudflare Pages through `wrangler.jsonc`. There is no build step; the repository root is the published directory.

## Turkish page (SEO)

`tr.html` (served at `/tr`) is the Turkish copy indexed by Google. After editing `index.html` or the Turkish strings in `script.js`, regenerate it with `python tests/tools/build_tr.py`.
