from __future__ import annotations

import os
from pathlib import Path
import re
from typing import cast, Any, Optional, Union
from urllib.parse import urlparse

from diskcache import Cache  # type: ignore
import requests

from .type_aliases import CSSClass, Url


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


def validate_local_file_reference(web_root: Path, local_path: Path) -> bool:
    possible_file_path = web_root / local_path
    if not possible_file_path.is_file():
        raise FileNotFoundError(str(possible_file_path))
    return True


def validate_remote_file_reference(url: Url, strict: bool = False) -> bool:
    url_parts = urlparse(url)
    if url_parts.hostname in REQUEST_IGNORE_FAILURES:
        return True
    if strict:
        print(f"- Checking url {url}")
        if REQUEST_CACHE.get(url):
            print("  * found in cache")
            return True
        try:
            requests.head(url, **REQUESTS_ARGS).raise_for_status()
        except requests.exceptions.HTTPError:
            requests.get(url, **REQUESTS_ARGS).raise_for_status()
        REQUEST_CACHE.set(url, True, expire=REQUEST_CACHE_TTL)
    return True


def validate_file_reference(web_root: Path, file_ref: Union[Path, Url],
                            strict: bool = False) -> bool:
    url_parts = urlparse(str(file_ref))
    if url_parts.scheme:
        return validate_remote_file_reference(cast(str, file_ref), strict)
    return validate_local_file_reference(web_root, Path(file_ref))


def to_css_class(text: str) -> Optional[CSSClass]:
    intermediate_text = text.strip().lower().replace(" ", "-")
    stubbed_text = re.sub(r'[^\w-]', '', intermediate_text, flags=re.ASCII)
    text_wo_dash_runs = re.sub(r'-+', '-', stubbed_text)
    return text_wo_dash_runs.strip("-")
