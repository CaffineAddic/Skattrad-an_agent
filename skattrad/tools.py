"""
Tools for Skattråd — Swedish Compliance Agent

fetch_page_content: fetches and cleans text from any URL.
Used to read full articles from Skatteverket, Bolagsverket, verksamt.se
after google_search has identified the relevant pages.
"""

import re
import urllib.request
import urllib.error
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    """Lightweight HTML → plain text extractor. No dependencies beyond stdlib."""

    SKIP_TAGS = {"script", "style", "nav", "footer", "header", "aside"}

    def __init__(self):
        super().__init__()
        self._skip = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip == 0:
            stripped = data.strip()
            if stripped:
                self.chunks.append(stripped)

    def get_text(self) -> str:
        raw = " ".join(self.chunks)
        # Collapse whitespace
        return re.sub(r"\s{2,}", " ", raw).strip()


def fetch_page_content(url: str) -> dict:
    """
    Fetch and extract the main text content from a webpage URL.
    Use this after google_search to read the full content of a relevant page
    from Skatteverket, Bolagsverket, verksamt.se, or riksdagen.se.

    Prefer this over relying on search snippets alone — full page content
    contains exact thresholds, calculation rules, and legal references.

    Args:
        url: The full URL of the page to fetch (must start with https://)

    Returns:
        dict with keys:
          - url: the fetched URL
          - content: extracted plain text (first 4000 chars)
          - status: "ok" or "error"
          - error: error message if status is "error"
    """
    TRUSTED_DOMAINS = (
        "skatteverket.se",
        "bolagsverket.se",
        "verksamt.se",
        "riksdagen.se",
        "government.se",
        "tillvaxtverket.se",
        "pts.se",
    )

    if not any(domain in url for domain in TRUSTED_DOMAINS):
        return {
            "url": url,
            "status": "error",
            "error": (
                f"Domain not in trusted list. Only fetching from: {', '.join(TRUSTED_DOMAINS)}. "
                "Use google_search to find pages on these domains first."
            ),
            "content": "",
        }

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (compatible; SkattradBot/1.0; "
                    "+https://github.com/skattrad)"
                )
            },
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            raw_html = response.read().decode("utf-8", errors="replace")

        parser = _TextExtractor()
        parser.feed(raw_html)
        text = parser.get_text()

        return {
            "url": url,
            "status": "ok",
            "content": text[:4000],  # keep within token budget
            "content_length": len(text),
            "truncated": len(text) > 4000,
        }

    except urllib.error.HTTPError as e:
        return {"url": url, "status": "error", "error": f"HTTP {e.code}: {e.reason}", "content": ""}
    except urllib.error.URLError as e:
        return {"url": url, "status": "error", "error": f"URL error: {e.reason}", "content": ""}
    except Exception as e:
        return {"url": url, "status": "error", "error": str(e), "content": ""}
