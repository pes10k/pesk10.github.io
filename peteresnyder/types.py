import dataclasses
import html
from pathlib import Path
from typing import Optional, Tuple

from .helpers import to_css_class
from .type_aliases import CSSClass, Html, Url


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
    url: Url | Path
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
    url: Optional[Url | Path] = None

    def title_classes(self) -> list[CSSClass]:
        text_to_stub = self.abbr or self.title
        return ["venue-title", f"venue-title-{to_css_class(text_to_stub)}"]

    def to_html(self) -> Html:
        esc_title = html.escape(self.title)
        html_str = ""
        css_classes = " ".join(self.title_classes())

        if self.abbr:
            esc_abbr = html.escape(self.abbr)
            html_str += (
                f'<abbr class="{css_classes}" ' +
                f'title="{esc_title}">{esc_abbr}</abbr>'
            )
        else:
            html_str += f'<span class="{css_classes}">{esc_title}</span>'

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
