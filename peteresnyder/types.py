import dataclasses
import datetime
import html
import os
from pathlib import Path
import sys
from typing import Any, Optional, Tuple, Union
from urllib.parse import urlparse

from diskcache import Cache  # type: ignore
import requests

Html = str
Url = str
Year = int
Date = Union[Year, datetime.datetime]
CSSClass = str
TalkType = str


def should_strict_validate() -> bool:
    return "--verbose" in sys.argv


REQUESTS_ARGS: dict[str, Any] = {
    "timeout": 5,
    "headers": {
        # pylint: disable-next=line-too-long
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }
}
REQUEST_CACHE_TTL: int = 60 * 60 * 24
REQUEST_CACHE: Cache = Cache(Path(f"{os.getcwd()}/.request-cache"))
REQUEST_IGNORE_FAILURES: list[Url] = [
    "www.fastcompany.com",
    "www.inc.com",
    "adage.com",
]


def is_path_valid(path: str) -> bool:
    url_parts = urlparse(path)
    if url_parts.scheme:
        if url_parts.hostname in REQUEST_IGNORE_FAILURES:
            return True
        if should_strict_validate():
            print(f"- Checking url {path}")
            if REQUEST_CACHE.get(path):
                print("  * found in cache")
                return True
            try:
                requests.head(path, **REQUESTS_ARGS).raise_for_status()
            except requests.exceptions.HTTPError:
                requests.get(path, **REQUESTS_ARGS).raise_for_status()
            REQUEST_CACHE.set(path, True, expire=REQUEST_CACHE_TTL)
        return True
    # Otherwise, treat it as a file path, and make sure that file exists
    return os.path.isfile(path)


def raise_path_validation_error(path: str) -> None:
    raise ValueError(f"{path} is not a valid url or local path")


def throw_if_invalid_path(path: str) -> None:
    if not is_path_valid(path):
        raise_path_validation_error(path)


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

    def __post_init__(self) -> None:
        throw_if_invalid_path(self.url)

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

    def __post_init__(self) -> None:
        if self.url:
            throw_if_invalid_path(self.url)

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
        if title in SPECIAL_NOTE_DEFS:
            self.title, self.css_class = SPECIAL_NOTE_DEFS[title]
        else:
            self.title = title
            self.css_class = None

    def to_html(self) -> Html:
        span_classes = ["label"]
        if self.css_class:
            span_classes.append(self.css_class)

        classes_markup = ' '.join(span_classes)
        return (
            f'<span class="{classes_markup}">' +
            html.escape(self.title) +
            "</span>"
        )


LINK_CLASS_PREFIXES: dict[str, CSSClass] = {
    "#fix:": "label-warning"
}


@dataclasses.dataclass
class Link:
    title: str
    url: Url
    css_class: Optional[CSSClass] = None

    def __post_init__(self) -> None:
        if self.title.startswith("#"):
            for prefix, a_css_class in LINK_CLASS_PREFIXES.items():
                if self.title.startswith(prefix):
                    self.title = self.title[1:]
                    self.css_class = a_css_class
                    break
            if not self.css_class:
                raise ValueError(f"Couldn't match {self.title} with a prefix")
        throw_if_invalid_path(self.url)

    def to_html(self) -> Html:
        default_label_class = 'label-default'
        if self.css_class is not None:
            label_class = self.css_class
        else:
            label_class = default_label_class
        start_tag = f'<span class="label {label_class} pub-link">'
        end_tag = '</span>'
        title_text = html.escape(self.title)
        return f'{start_tag}<a href="{self.url}">{title_text}</a>{end_tag}'
