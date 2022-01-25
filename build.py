#!/usr/bin/env python3
import json
from pathlib import Path
import sys
from typing import Any, Dict

from peteresnyder.indent import Indenter
from peteresnyder.items import BlogItem, CodeItem, InvolvementItem
from peteresnyder.items import PressItem, PublicationItem
from peteresnyder.items import TalksItem, WritingItem

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
    section_html = indenter.to_html()
    TEMPLATE_INDEX_HTML_TEXT = TEMPLATE_INDEX_HTML_TEXT.replace(
        "{{" + section_file.stem + "}}", section_html)

print(TEMPLATE_INDEX_HTML_TEXT)