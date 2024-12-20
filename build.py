#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys
from typing import Any, Dict

from peteresnyder.indent import Indenter
from peteresnyder.items import BlogItem, CodeItem, InvolvementItem
from peteresnyder.items import PressItem, PublicationItem
from peteresnyder.items import TalksItem, WritingItem, NonTechWriting

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
    "--output", "-o",
    type=Path,
    default=Path("./index.html"),
    help="Path to write the resulting HTML to. If passed '-', output is "
         "written to STDOUT.")
ARGS = parser.parse_args()

BASE_PATH = Path(sys.argv[0]).parent.resolve()
DATA_DIR = Path(".", "data")
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
        item.validate(BASE_PATH)
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
