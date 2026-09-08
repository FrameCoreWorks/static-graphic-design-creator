#!/usr/bin/env python3
"""Read-only lookup for the bundled Event Poster Design Codes catalog."""

import argparse
import json
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "references/event-poster-design-codes.json"
CATALOG_COMMANDS = {"/kody", "kody", "/codes", "codes"}


def normalize(value):
    return " ".join(value.split()).casefold()


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def entries(catalog):
    return [
        {**code, "category_number": category["number"],
         "category_name": category["name"], "pdf_page": category["pdf_page"]}
        for category in catalog["categories"] for code in category["codes"]
    ]


def resolve_code(value, catalog):
    """Exact ID/name/slash shorthand/complete-line lookup; no fuzzy selection."""
    key = normalize(value)
    if not key:
        return None
    matches = [entry for entry in entries(catalog)
               if key in {normalize(entry["id"]), normalize(entry["code"]), normalize(entry["shorthand"]),
                          normalize(entry["code"][1:-len(" /rebuild")])}]
    return matches[0] if len(matches) == 1 else None


def select_category(value, catalog):
    key = normalize(value)
    return [category for category in catalog["categories"]
            if key in {str(category["number"]), f'{category["number"]:02d}',
                       normalize(category["name"])}]


def search(value, catalog):
    key = normalize(value)
    if not key:
        return []
    return [entry for entry in entries(catalog)
            if any(key in normalize(text) for text in
                   [entry["code"], entry["category_name"],
                    entry["interpretation"]["description_pl"], entry["interpretation"]["description_en"]])]


def catalog_markdown(catalog, language="pl"):
    """Full grouped collection, including every code and its interpreted benefit."""
    if language not in {"pl", "en"}:
        raise ValueError("language must be pl or en")
    intro = ("200 kodów w 20 kategoriach. Nazwy: John Savage AI; opisy i zastosowania: interpretacje FrameCore Works. "
             "Dla nowego promptu można użyć skrótu /Nazwa; /Nazwa /rebuild oznacza kierunek przebudowy istniejącego plakatu."
             if language == "pl" else
             "200 codes in 20 categories. Names: John Savage AI; descriptions and uses: FrameCore Works interpretations. "
             "Use /Name for a new prompt, or /Name /rebuild as the direction for rebuilding an existing poster.")
    lines = [intro, ""]
    heading = "| Kod | Styl i zastosowanie |" if language == "pl" else "| Code | Style and use |"
    for category in catalog["categories"]:
        lines.extend([f'### {category["number"]:02d} {category["name"]}', "", heading, "| --- | --- |"])
        for entry in category["codes"]:
            description = entry["interpretation"]["description_" + language].replace("|", "\\|")
            lines.append(f'| `{entry["code"]}` | {description} |')
        lines.append("")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--code", help="Complete code line, exact code name or local EP ID")
    group.add_argument("--category", help="Category number or exact category name")
    group.add_argument("--query", help="Substring search; returns candidates without selecting one")
    group.add_argument("--list-categories", action="store_true")
    group.add_argument("--command", help="/kody, kody, /codes or codes: full grouped catalog with descriptions")
    parser.add_argument("--language", choices=["pl", "en"], default="pl", help="Catalog response language")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        if args.command is not None:
            if normalize(args.command) not in CATALOG_COMMANDS:
                print(json.dumps({"status": "unknown_command", "accepted": sorted(CATALOG_COMMANDS)}))
                return 1
            print(catalog_markdown(catalog, args.language))
            return 0
        if args.code is not None:
            entry = resolve_code(args.code, catalog)
            result = {"status": "matched" if entry else "not_found", "match": entry}
        elif args.category is not None:
            categories = select_category(args.category, catalog)
            result = {"status": "matched" if categories else "not_found", "categories": categories}
        elif args.query is not None:
            candidates = search(args.query, catalog)
            result = {"status": "candidates" if candidates else "not_found", "selected": None,
                      "matches": candidates}
        else:
            result = {"status": "listed", "categories": [
                {"number": c["number"], "name": c["name"], "pdf_page": c["pdf_page"],
                 "count": len(c["codes"])} for c in catalog["categories"]]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result["status"] == "not_found" else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "catalog_error", "error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
