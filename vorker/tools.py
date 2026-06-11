"""
Tools for Vorker Compliance — Swedish SME compliance agent.
"""

import re
import urllib.error
import urllib.request
from html.parser import HTMLParser

from .sources import CURATED_SOURCES

TRUSTED_DOMAINS = (
    "skatteverket.se",
    "bolagsverket.se",
    "verksamt.se",
    "riksdagen.se",
    "government.se",
    "arbetsgivarverket.se",
    "tillvaxtverket.se",
)


class _TextExtractor(HTMLParser):
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
        return re.sub(r"\s{2,}", " ", raw).strip()


def _normalize_topic(topic: str) -> str:
    return topic.strip().lower().replace(" ", "_")


def get_recommended_sources(topic: str) -> dict:
    """
    Return curated authoritative URLs for a Swedish compliance topic.
    Use when the user asks about aktieägaravtal, hembudsförbehåll,
    karensavdrag, or cross-border VAT — then fetch those pages for grounding.

    Args:
        topic: Compliance topic keyword, e.g. 'karensavdrag', 'aktieägaravtal',
               'vat_cross_border', 'hembudsförbehåll', 'moms_utlandet'

    Returns:
        dict with topic label, hint, and list of recommended URLs
    """
    key = _normalize_topic(topic)
    if key not in CURATED_SOURCES:
        matches = [
            name
            for name, data in CURATED_SOURCES.items()
            if key in name or name in key
        ]
        if matches:
            key = matches[0]
        else:
            return {
                "status": "not_found",
                "topic": topic,
                "available_topics": list(CURATED_SOURCES.keys()),
                "message": "Unknown topic. Use google_search or pick an available topic.",
            }

    entry = CURATED_SOURCES[key]
    return {
        "status": "ok",
        "topic": entry["topic"],
        "hint": entry["hint"],
        "urls": entry["urls"],
        "message": "Fetch these URLs with fetch_page_content before answering.",
    }


def fetch_page_content(url: str) -> dict:
    """
    Fetch and extract plain text from a trusted Swedish authority webpage.
    Use after google_search or get_recommended_sources to read full regulatory content.

    Args:
        url: HTTPS URL on skatteverket.se, bolagsverket.se, verksamt.se, etc.

    Returns:
        dict with url, status ('ok' or 'error'), content (up to 4000 chars), and error if any
    """
    if not url.startswith("https://"):
        return {
            "url": url,
            "status": "error",
            "error": "URL must start with https://",
            "content": "",
        }

    if not any(domain in url for domain in TRUSTED_DOMAINS):
        return {
            "url": url,
            "status": "error",
            "error": f"Domain not trusted. Allowed: {', '.join(TRUSTED_DOMAINS)}",
            "content": "",
        }

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (compatible; VorkerCompliance/1.0; "
                    "+https://github.com/CaffineAddic/Vorker)"
                )
            },
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            raw_html = response.read().decode("utf-8", errors="replace")

        parser = _TextExtractor()
        parser.feed(raw_html)
        text = parser.get_text()

        return {
            "url": url,
            "status": "ok",
            "content": text[:4000],
            "content_length": len(text),
            "truncated": len(text) > 4000,
        }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": "error", "error": f"HTTP {e.code}: {e.reason}", "content": ""}
    except urllib.error.URLError as e:
        return {"url": url, "status": "error", "error": f"URL error: {e.reason}", "content": ""}
    except Exception as e:
        return {"url": url, "status": "error", "error": str(e), "content": ""}
