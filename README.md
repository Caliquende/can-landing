# can-landing

Bilingual static personal landing page for Hamdi Can Ernalbantogullari's QA Engineer, Test Automation Engineer, and SDET profile.

## Overview

This repository contains a deployment-ready single-page site built with plain HTML, CSS, and JavaScript. It includes English and Turkish content, profile summary sections, QA/SDET skill highlights, project cards, contact actions, and basic SEO/Open Graph metadata.

There is no build step and no package manager dependency. The site can be opened directly in a browser or deployed as static files.

## Repository Structure

```text
.
├── index.html       # Page content, semantic structure, and metadata
├── style.css        # Responsive visual design
├── script.js        # Language switching, navigation, and small UI helpers
├── cv.md            # Source CV/profile content
├── wrangler.jsonc   # Cloudflare Workers/Pages configuration
└── README.md        # Project documentation
```

## Local Preview

Open `index.html` directly in a browser, or serve the folder with any static server:

```powershell
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment

The repository is suitable for GitHub Pages, Netlify, Vercel, Cloudflare Pages, or any static hosting provider.

Before publishing, keep the public page copy aligned with `cv.md` and verify both language modes.

## Validation

Check the page after every content or style update:

- Open the page on desktop and mobile widths.
- Switch between English and Turkish.
- Verify contact links and copy-to-clipboard behavior.
- Confirm metadata in `index.html` still matches the current public profile.
