import re

EXPECTED_TITLE = re.compile(r"Hamdi Can Ernalbanto")

MAIN_SECTIONS = ["about", "skills", "experience", "projects", "contact"]

LANGUAGE = {
    "english": {
        "code": "en",
        "heading": "About",
        "title": re.compile(r"Software QA"),
        "description": re.compile(r"QA Engineer"),
    },
    "turkish": {
        "code": "tr",
        "heading": "Hakkımda",
        "title": re.compile(r"Yazılım Kalite Güvence"),
        "description": re.compile(r"Yazılım testleri"),
    },
}

LINKS = {
    "email": re.compile(r"^mailto:"),
    "linkedin": re.compile(r"linkedin\.com"),
    "github": re.compile(r"github\.com"),
}

OG_IMAGE = re.compile(r"favicon\.svg")

PROJECT_TITLES = [
    "Python Test Automation",
    "OKX Spot Trading Bot",
    "ResearchFlow Android",
    "WasteWisely",
    "New Marketplace",
]

REFERENCE_NAMES = [
    "Barış Karaman",
    "Fulden Karameşe",
    "Mustafa İnaç",
    "Onur Abdullah Gördük",
]
