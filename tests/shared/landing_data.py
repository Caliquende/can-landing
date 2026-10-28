import re

EXPECTED_TITLE = re.compile(r"Hamdi Can Ernalbanto")

MAIN_SECTIONS = ["about", "experience", "skills", "projects", "contact"]

LANGUAGE = {
    "english": {
        "code": "en",
        "heading": "Experience",
        "title": re.compile(r"QA Engineer"),
        "description": re.compile(r"QA Engineer"),
    },
    "turkish": {
        "code": "tr",
        "heading": "Deneyim",
        "title": re.compile(r"QA Mühendisi"),
        "description": re.compile(r"QA Mühendisi"),
    },
}

LINKS = {
    "email": re.compile(r"^mailto:"),
    "linkedin": re.compile(r"linkedin\.com"),
    "github": re.compile(r"github\.com"),
}

OG_IMAGE = re.compile(r"can\.png")

PROJECT_TITLES = [
    "Python Test Automation",
    "OKX Spot Trading Bot",
    "ResearchFlow Android",
    "WasteWisely",
    "New Marketplace",
]

REFERENCE_NOTES = {
    "english": re.compile(r"references available upon request", re.IGNORECASE),
    "turkish": re.compile(r"talep üzerine paylaşılır"),
}

QA_NOTES = {
    "english": re.compile(r"This page is tested too"),
    "turkish": re.compile(r"Bu sayfa da test ediliyor"),
}

CV_FILE = re.compile(r"assets/cv\.pdf$")
CV_DOWNLOAD_NAME = "Hamdi Can Ernalbantogullari CV.pdf"
PORTRAIT_FILE = re.compile(r"assets/can\.png$")

PAGE_ASSETS = [
    "style.css",
    "script.js",
    "favicon.svg",
    "assets/can.png",
    "assets/cv.pdf",
]

MIN_EXTERNAL_LINKS = 2
