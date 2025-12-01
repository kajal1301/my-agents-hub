# agents/preview.py

from __future__ import annotations
import re
from typing import Dict, List

def build_inlined_preview_html(artifacts: List[Dict]) -> str:
    """
    Given code artifacts (list of dicts with {path, content}),
    return a single HTML string with <style> and <script> inlined.
    Supports simple cases:
      - index.html referencing ./style.css and ./index.js
      - relative paths in the same folder
    """
    by_path = {a["path"].lstrip("./"): a["content"] for a in artifacts}
    # pick candidate index
    index_candidates = [p for p in by_path if p.lower().endswith("index.html")]
    if not index_candidates:
        # create a minimal index if none exists
        return """<!doctype html><html><head><meta charset="utf-8">
<title>Preview</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>html,body{margin:0;padding:0;font:14px system-ui} .wrap{padding:16px}</style>
</head><body><div class="wrap"><h2>Preview</h2><p>No index.html found.</p></div></body></html>"""
    index_path = sorted(index_candidates)[0]
    html = by_path[index_path]

    # inline simple <link rel="stylesheet" href="...">
    def _inline_css(m):
        href = m.group(1).lstrip("./")
        css = by_path.get(href, "")
        return f"<style>\n{css}\n</style>"

    html = re.sub(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\'][^>]*>',
                  _inline_css, html, flags=re.IGNORECASE)

    # inline simple <script src="..."></script>
    def _inline_js(m):
        src = m.group(1).lstrip("./")
        js = by_path.get(src, "")
        return f"<script>\n{js}\n</script>"

    html = re.sub(r'<script[^>]+src=["\']([^"\']+)["\'][^>]*>\s*</script>',
                  _inline_js, html, flags=re.IGNORECASE)

    # ensure viewport meta for responsiveness
    if 'name="viewport"' not in html:
        html = html.replace("<head>", '<head><meta name="viewport" content="width=device-width,initial-scale=1">')

    return html
