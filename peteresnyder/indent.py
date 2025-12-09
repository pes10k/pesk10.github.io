from __future__ import annotations

from typing import List

from .type_aliases import Html

class Indenter:
    level: int
    chars: str
    markup: List[Html]

    def __init__(self, level: int = 0, chars: str = "    ") -> None:
        self.level = level
        self.chars = chars
        self.markup = []

    def add(self, html: Html) -> Indenter:
        self.markup.append((self.level * self.chars) + html)
        return self

    def up(self) -> Indenter:
        self.level += 1
        return self

    def down(self) -> Indenter:
        self.level -= 1
        return self

    def to_html(self) -> Html:
        return "\n".join(self.markup)
