#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

from peteresnyder.indent import Indenter
from peteresnyder.items import BlogItem, CodeItem, InvolvementItem
from peteresnyder.items import PressItem, PublicationItem
from peteresnyder.items import TalksItem, WritingItem, NonTechWriting

DEFAULT_ROOT = Path(".", "web")

parser = argparse.ArgumentParser(
    prog="Build www.peteresnyder.com",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "--validate",
    action="store_true",
    default=False,
    help="Don't print the generated page, just validate that the page seems "
         "to build correctly. Exits with process code 0 if the page builds "
         "successfully, and 1 otherwise.")
parser.add_argument(
    "--strict",
    action="store_true",
    default=False,
    help="Extend validation to check that referenced URLs return 20X codes.")
parser.add_argument(
    "--root", "-r",
    type=Path,
    default=DEFAULT_ROOT,
    help="Default path to use as the root of the web page build.")
parser.add_argument(
    "--output", "-o",
    type=Path,
    default=DEFAULT_ROOT / "index.html",
    help="Path to write the resulting HTML to. If passed '-', output is "
         "written to STDOUT.")
ARGS = parser.parse_args()

DATA_DIR = Path("./data")
TEMPLATE_DIR = DATA_DIR / Path("templates")
SECTIONS_DIR = DATA_DIR / Path("sections")
TEMPLATE_INDEX_HTML_TEXT = (TEMPLATE_DIR / Path("index.html")).read_text()

FILE_TYPE_MAPPING: Dict[str, Any] = {
    "press": [PressItem, 5],
    "blog": [BlogItem, 5],
    "involvement": [InvolvementItem, 7],
    "publications": [PublicationItem, 5],
    "talks": [TalksItem, 4],
    "writing": [WritingItem, 5],
    "code": [CodeItem, 5],
    "nontech": [NonTechWriting, 5],
}

for section_file in SECTIONS_DIR.iterdir():
    if section_file.stem not in FILE_TYPE_MAPPING:
        continue
    section_type, indent_level = FILE_TYPE_MAPPING[section_file.stem]
    section_data = json.load(section_file.open())
    items = section_type.list_from_json(section_data)
    for item in items:
        item.validate(ARGS.root, ARGS.strict)
    items_sorted = section_type.sort(items)
    indenter = Indenter(indent_level, "    ")
    section_type.add_list_html(items_sorted, indenter)
    TEMPLATE_INDEX_HTML_TEXT = TEMPLATE_INDEX_HTML_TEXT.replace(
        "{{" + section_file.stem + "}}", indenter.to_html())

if ARGS.validate:
    sys.exit(0)

if ARGS.output.name == "-":
    sys.stdout.write(TEMPLATE_INDEX_HTML_TEXT)
else:
    ARGS.output.write_text(TEMPLATE_INDEX_HTML_TEXT)
sys.exit(0)
