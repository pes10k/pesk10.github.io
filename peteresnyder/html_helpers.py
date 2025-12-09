from __future__ import annotations

import re
from typing import Optional

from .type_aliases import CSSClass

def to_css_class(text: str) -> Optional[CSSClass]:
    intermediate_text = text.strip().lower().replace(" ", "-")
    stubbed_text = re.sub(r'[^\w-]', '', intermediate_text, flags=re.ASCII)
    text_wo_dash_runs = re.sub(r'-+', '-', stubbed_text)
    return text_wo_dash_runs.strip("-")
