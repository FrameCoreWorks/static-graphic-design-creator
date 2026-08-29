#!/usr/bin/env python3
"""Check curated research anchors without making ordinary contract CI network-dependent."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = (
    ROOT / ".agents" / "skills" / "static-graphic-design-creator" / "references" / "poster-movements-and-production-atlas.md",
    ROOT / ".agents" / "skills" / "static-graphic-design-creator" / "references" / "poster-style-translation-catalog.md",
)
URL_PATTERN = re.compile(r"https?://[^\s)<]+")


def collect_urls() -> list[str]:
    urls: set[str] = set()
    for source in SOURCE_FILES:
        if not source.is_file():
            raise AssertionError(f"Missing reference-anchor source: {source.relative_to(ROOT)}")
        urls.update(URL_PATTERN.findall(source.read_text(encoding="utf-8")))
    return sorted(urls)


def check_inventory(urls: list[str]) -> None:
    if len(urls) < 16:
        raise AssertionError(f"Expected at least 16 curated source anchors, found {len(urls)}")
    if any(not url.startswith("https://") for url in urls):
        raise AssertionError("Every curated source anchor must use HTTPS")


def request(url: str) -> int:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "FrameCoreWorks-SourceAnchorCheck/1.0", "Accept": "text/html,*/*"},
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.status


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-inventory", action="store_true")
    args = parser.parse_args()

    urls = collect_urls()
    check_inventory(urls)
    if args.check_inventory:
        print(f"reference-anchor inventory passed: {len(urls)} URLs")
        return

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(request, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                status = future.result()
                if not 200 <= status < 400:
                    failures.append(f"{url} returned HTTP {status}")
            except urllib.error.HTTPError as error:
                if error.code not in {401, 403, 405, 429}:
                    failures.append(f"{url}: {error}")
            except (urllib.error.URLError, TimeoutError) as error:
                failures.append(f"{url}: {error}")

    if failures:
        print("reference-anchor check failed:", *failures, sep="\n", file=sys.stderr)
        raise SystemExit(1)
    print(f"reference-anchor reachability passed: {len(urls)} URLs")


if __name__ == "__main__":
    main()
