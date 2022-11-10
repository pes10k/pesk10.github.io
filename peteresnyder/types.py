import collections
import dataclasses
import datetime
import html
import os
from typing import Callable, cast, Dict, NamedTuple, Optional, Union

Html = str
Url = str
Year = int
Date = Union[Year, datetime.datetime]


@dataclasses.dataclass
class TalkType:
    title: str

    def to_html(self) -> Html:
        return f"<span class='pub-type'>{html.escape(self.title)}</span>"


@dataclasses.dataclass
class Author:
    title: str
    abbr: Optional[str] = None

    def to_html(self) -> Html:
        if self.abbr == "@me":
            return f"<span class='me'>{html.escape(self.title)}</span>"
        return html.escape(self.title)


@dataclasses.dataclass
class Source:
    title: str
    url: Url
    abbr: str

    def to_html(self) -> Html:
        return (
            f"<a href='{self.url}' class='source source-{self.abbr[1:]}'>" +
            html.escape(self.title) +
            "</a>"
        )


@dataclasses.dataclass
class Venue:
    title: str
    abbr: Optional[str] = None
    suffix: Optional[str] = None

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

        return html_str


class LinkValidator(NamedTuple):
    check: Callable[[str], bool]
    name: str


LINK_VALIDATORS: Dict[str, LinkValidator] = {
    "@slides": LinkValidator(os.path.isfile, "slides"),
    "@slides-keynote": LinkValidator(os.path.isfile, "slides (keynote)")
}


@dataclasses.dataclass
class PubNote:
    title: str

    def to_html(self) -> Html:
        return (
            "<span class='label label-primary'>" +
            html.escape(self.title) +
            "</span>"
        )


@dataclasses.dataclass
class Link:
    title: str
    url: Url

    def __post_init__(self) -> None:
        if self.title[0] != "@":
            return
        validator = LINK_VALIDATORS[self.title]
        if not validator.check(self.url):
            raise ValueError(f"{self.url} is not a valid {self.title}")
        self.title = validator.name

    def to_html(self) -> Html:
        return f"<a href='{self.url}'>{html.escape(self.title)}</a>"
