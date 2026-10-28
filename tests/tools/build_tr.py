"""Regenerate tr.html, served at /tr (the Turkish, search-indexable copy of the page).

Run after changing index.html or the Turkish strings in script.js:
    python tests/tools/build_tr.py
It renders index.html in Chromium, switches to TR and saves the result with
Turkish URLs, canonical and structured data.
"""
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://can.is-a.dev"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto((ROOT / "index.html").as_uri())
    page.click("[data-lang='tr']")
    html = "<!doctype html>\n" + page.evaluate("document.documentElement.outerHTML")
    browser.close()

html = html.replace(f'<link rel="canonical" href="{BASE}/">', f'<link rel="canonical" href="{BASE}/tr">')
html = html.replace(f'property="og:url" content="{BASE}/"', f'property="og:url" content="{BASE}/tr"')
html = html.replace('content="en_US">', 'content="__EN__">').replace('content="tr_TR">', 'content="en_US">').replace('content="__EN__">', 'content="tr_TR">')
html = html.replace('alt="Hamdi Can Ernalbantoğulları"', 'alt="Hamdi Can Ernalbantoğulları — QA Mühendisi"')

def fix_ld(match):
    data = json.loads(match.group(1))
    data["url"] = f"{BASE}/tr"
    data["jobTitle"] = "QA Mühendisi & SDET"
    data["knowsAbout"] = ["Yazılım Testi", "Test Otomasyonu", "Regresyon Testi", "Python", "Selenium", "Pytest", "Playwright", "Jira", "Smart TV Test"]
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"

html = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, html, flags=re.S)
(ROOT / "tr.html").write_text(html, encoding="utf-8")
print("wrote tr.html")
