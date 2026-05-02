from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
BASE_URL = (ROOT_DIR / "index.html").as_uri()

DESKTOP_VIEWPORT = {"width": 1280, "height": 720}
MOBILE_VIEWPORT = {"width": 390, "height": 844}
TABLET_VIEWPORT = {"width": 768, "height": 1024}
