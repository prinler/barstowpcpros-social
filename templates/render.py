"""Render an HTML template to a 1080x1350 PNG.
Usage: python3 templates/render.py templates/<name>.html out.png
Templates reference ../brand/logo.png and common.css relative to templates/."""
import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto(src.as_uri()); pg.wait_for_timeout(300); pg.screenshot(path=out); b.close()
