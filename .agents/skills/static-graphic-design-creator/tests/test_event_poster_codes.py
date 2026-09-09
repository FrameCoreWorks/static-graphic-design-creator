"""Collection fidelity and read-only lookup regression tests (no generation)."""

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/event_poster_codes.py"
spec = importlib.util.spec_from_file_location("event_poster_codes", SCRIPT)
lookup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup)

# Independently confirmed from both PyMuPDF and spatial pdfplumber extraction.
SOURCE_SHA256 = "9e89970dfc5f482d3477b3efacc3ccef5382e737d0c58be2cc7aec320194e80f"
CODE_LINES_SHA256 = "da4fd222eb075f9188394434d3ea14753b77acf7d2b6fd93b4834dc1bacf4485"
CATEGORIES = [
    "MODERNIST SYSTEMS", "PRINT IMPERFECTIONS", "INDUSTRIAL BRUTALISM",
    "EDITORIAL FASHION", "COLLAGE EPHEMERA", "NIGHTLIFE NEON", "LUXURY CULTURE",
    "ZINE UNDERGROUND", "CINEMATIC PHOTOGRAPHY", "HISTORICAL GLAMOUR",
    "SPORTS BROADCAST", "MATERIAL TYPOGRAPHY", "STREET ACTIVISM",
    "MUSEUM INSTITUTIONAL", "SURREAL SPATIAL", "GLOBAL PRINT TRADITIONS",
    "DIGITAL CHROME FUTURE", "FOLK CRAFT", "NEWSPAPER PUBLISHING", "MOTION OPTICAL",
]


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = lookup.load_catalog()
        cls.entries = lookup.entries(cls.catalog)

    def test_complete_exact_source_lines(self):
        codes = [e["code"] for e in self.entries]
        self.assertEqual(len(codes), 200)
        self.assertEqual(len(set(codes)), 200)
        self.assertEqual(hashlib.sha256(("\n".join(codes) + "\n").encode()).hexdigest(),
                         CODE_LINES_SHA256)
        self.assertEqual(self.catalog["canonical_code_lines_sha256"], CODE_LINES_SHA256)
        for code in codes:
            self.assertRegex(code, r"^/[^/\n]+ /rebuild$")

    def test_category_membership_order_and_pages(self):
        categories = self.catalog["categories"]
        self.assertEqual([c["name"] for c in categories], CATEGORIES)
        self.assertEqual([c["number"] for c in categories], list(range(1, 21)))
        for number, category in enumerate(categories, 1):
            self.assertEqual(category["pdf_page"], (number - 1) // 4 + 2)
            self.assertEqual(len(category["codes"]), 10)
            self.assertEqual([c["id"] for c in category["codes"]],
                             [f"EP{i:03d}" for i in range((number - 1) * 10 + 1, number * 10 + 1)])

    def test_provenance_and_source_contract(self):
        self.assertEqual(self.catalog["source"]["file_sha256"], SOURCE_SHA256)
        self.assertEqual(self.catalog["source"]["page_count"], 6)
        self.assertEqual(self.catalog["source"]["author"], "John Savage AI")
        self.assertEqual(self.catalog["source_rebuild_contract"]["preserve"], ["factual content"])
        self.assertEqual(self.catalog["source_rebuild_contract"]["rebuild"],
                         ["layout", "hierarchy", "palette", "typography", "materials", "image treatment"])
        self.assertEqual(self.catalog["evidence_limits"]["native_generator_command_support"], "Unknown")

    def test_every_entry_round_trips(self):
        for entry in self.entries:
            for value in [entry["code"], entry["id"], entry["shorthand"], entry["code"][1:-len(" /rebuild")]]:
                self.assertEqual(lookup.resolve_code(value, self.catalog), entry)

    def test_english_source_descriptions_and_derived_shortcuts(self):
        descriptions = [e["interpretation"]["description_en"] for e in self.entries]
        self.assertEqual(len(set(descriptions)), 200)
        self.assertTrue(all(len(text.split()) >= 9 for text in descriptions))
        self.assertEqual(self.catalog["interpretation_provenance"]["languages"], ["en"])
        for entry in self.entries:
            self.assertEqual(set(entry["interpretation"]), {"description_en"})
            self.assertEqual(entry["shorthand"] + " /rebuild", entry["code"])
        self.assertEqual(self.catalog["interpretation_provenance"]["author"], "FrameCore Works")

    def test_full_catalog_contains_every_code_and_description(self):
        result = lookup.catalog_markdown(self.catalog)
        self.assertEqual(result, lookup.catalog_markdown(self.catalog, "en"))
        self.assertEqual(sum(line.startswith("### ") for line in result.splitlines()), 20)
        for entry in self.entries:
            self.assertEqual(result.count("`" + entry["code"] + "`"), 1)
            self.assertIn(entry["interpretation"]["description_en"], result)
        for language in ["pl", "es", "unsupported"]:
            with self.assertRaises(ValueError):
                lookup.catalog_markdown(self.catalog, language)

    def test_catalog_command_aliases(self):
        self.assertEqual(set(self.catalog["catalog_commands"]), lookup.CATALOG_COMMANDS)
        expected = lookup.catalog_markdown(self.catalog) + "\n"
        for command in ["/kody", "kody", "/codes", "codes", "  /CODES  "]:
            result = subprocess.run([sys.executable, str(SCRIPT), "--command", command], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.count(" /rebuild`"), 200)
            self.assertEqual(result.stdout, expected)
        result = subprocess.run([sys.executable, str(SCRIPT), "--command", "codes", "--language", "en"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count(" /rebuild`"), 200)
        self.assertIn("Style and use", result.stdout)
        localized = subprocess.run([sys.executable, str(SCRIPT), "--command", "/codes", "--language", "pl"], capture_output=True, text=True)
        self.assertEqual(localized.returncode, 2)
        self.assertEqual(localized.stdout, "")
        invalid = subprocess.run([sys.executable, str(SCRIPT), "--command", "/render"], capture_output=True, text=True)
        self.assertEqual(invalid.returncode, 1)
        self.assertEqual(json.loads(invalid.stdout)["status"], "unknown_command")

    def test_case_and_whitespace_keep_canonical_spelling(self):
        match = lookup.resolve_code("  /two   INK collision    /REBUILD  ", self.catalog)
        self.assertEqual(match["code"], "/Two Ink Collision /rebuild")
        self.assertEqual((match["id"], match["category_number"], match["pdf_page"]), ("EP011", 2, 2))

    def test_no_fuzzy_auto_selection_or_execution(self):
        for value in ["", " ", "/rebuild", "Bauhaus", "EP000", "EP201",
                      "/Imaginary Emerald Universe /rebuild", "$(touch unexpected)",
                      "/Two Ink Collision /rebuild /Film Noir Cabaret /rebuild"]:
            self.assertIsNone(lookup.resolve_code(value, self.catalog))
        self.assertEqual(len(lookup.search("Bauhaus", self.catalog)), 2)
        self.assertEqual(lookup.search("  ", self.catalog), [])

    def test_categories_have_no_fuzzy_selection(self):
        for value in ["20", "MOTION OPTICAL", " motion   optical "]:
            self.assertEqual(lookup.select_category(value, self.catalog)[0]["number"], 20)
        self.assertEqual(lookup.select_category("02", self.catalog)[0]["name"], "PRINT IMPERFECTIONS")
        self.assertEqual(lookup.select_category("PRINT", self.catalog), [])
        self.assertEqual(lookup.select_category("21", self.catalog), [])

    def test_cli_results_and_exit_codes(self):
        before = hashlib.sha256(lookup.CATALOG.read_bytes()).hexdigest()
        for args, status, exit_code in [
            (["--code", "EP200"], "matched", 0),
            (["--code", "EP999"], "not_found", 1),
            (["--category", "02"], "matched", 0),
            (["--query", "Bauhaus"], "candidates", 0),
            (["--list-categories"], "listed", 0),
        ]:
            result = subprocess.run([sys.executable, str(SCRIPT)] + args, capture_output=True, text=True)
            self.assertEqual(result.returncode, exit_code, result.stderr)
            output = json.loads(result.stdout)
            self.assertEqual(output["status"], status)
            if status == "candidates":
                self.assertIsNone(output["selected"])
                self.assertEqual(len(output["matches"]), 2)
            if status == "listed":
                self.assertEqual(sum(c["count"] for c in output["categories"]), 200)
        self.assertEqual(hashlib.sha256(lookup.CATALOG.read_bytes()).hexdigest(), before)
        self.assertIn("EP004", [e["id"] for e in lookup.search("Break one alignment", self.catalog)])


if __name__ == "__main__":
    unittest.main()
