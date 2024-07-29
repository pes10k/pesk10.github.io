import dataclasses
import datetime
import html
import os
from typing import Callable, NamedTuple, Optional, Tuple, Union

Html = str
Url = str
Year = int
Date = Union[Year, datetime.datetime]
CSSClass = str
TalkType = str


@dataclasses.dataclass
class Author:
    title: str
    abbr: Optional[str] = None

    def to_html(self) -> Html:
        if self.abbr == "@me":
            return f'<span class="me">{html.escape(self.title)}</span>'
        return html.escape(self.title)


@dataclasses.dataclass
class Source:
    title: str
    url: Url
    abbr: str

    def to_html(self) -> Html:
        return (
            f'<a href="{self.url}" class="source source-{self.abbr[1:]}">' +
            html.escape(self.title) +
            "</a>"
        )


@dataclasses.dataclass
class Venue:
    title: str
    abbr: Optional[str] = None
    suffix: Optional[str] = None
    url: Optional[Url] = None

    def to_html(self) -> Html:
        esc_title = html.escape(self.title)
        html_str = ""
        if self.abbr:
            esc_abbr = html.escape(self.abbr)
            html_str += f'<abbr title="{esc_title}">{esc_abbr}</abbr>'
        else:
            html_str += f'<span>{esc_title}</span>'

        if self.suffix:
            html_str += " " + html.escape(self.suffix)

        if self.url:
            html_str = f'<a href="{self.url}">{html_str}</a>'

        return html_str


SPECIAL_NOTE_DEFS: dict[str, Tuple[str, CSSClass]] = {
    "#best-paper": ("best paper", "label-primary"),
    "#short-paper": ("short paper", "label-success"),
}


@dataclasses.dataclass
class PubNote:
    title: str
    css_class: Optional[CSSClass]

    def __init__(self, title: str) -> None:
        if title.startswith("#"):
            self.title, self.css_class = SPECIAL_NOTE_DEFS[title]
        else:
            self.title = title
            self.css_class = None

    def to_html(self) -> Html:
        span_classes = ["label"]
        if self.css_class:
            span_classes.append(self.css_class)

        return (
            f'<span class="{' '.join(span_classes)}">' +
            html.escape(self.title) +
            "</span>"
        )


class LinkValidator(NamedTuple):
    check: Callable[[str], bool]
    name: str


LINK_VALIDATORS: dict[str, LinkValidator] = {
    "@slides": LinkValidator(os.path.isfile, "slides"),
    "@slides-keynote": LinkValidator(os.path.isfile, "slides (keynote)")
}


@dataclasses.dataclass
class Link:
    title: str
    url: Url

    def __post_init__(self) -> None:
        if not self.title.startswith("@"):
            return
        validator = LINK_VALIDATORS[self.title]
        if not validator.check(self.url):
            raise ValueError(f"{self.url} is not a valid {self.title}")
        self.title = validator.name

    def to_html(self) -> Html:
        return f'<a href="{self.url}">{html.escape(self.title)}</a>'
