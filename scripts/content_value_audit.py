#!/usr/bin/env python3
"""Auditoría rápida para detectar señales de "contenido de poco valor"."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MIN_WORDS = 600
MIN_INTERNAL_LINKS = 5


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.text: list[str] = []
        self.in_script_or_style = False

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.in_script_or_style = True

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.in_script_or_style = False

    def handle_data(self, data):
        if not self.in_script_or_style:
            self.text.append(data)


def extract_words(html: str) -> int:
    parser = TextExtractor()
    parser.feed(html)
    text = " ".join(parser.text)
    tokens = re.findall(r"\b[\wáéíóúñüÁÉÍÓÚÑÜ]{2,}\b", text, flags=re.UNICODE)
    return len(tokens)


def count_internal_links(html: str) -> int:
    links = re.findall(r"href=[\"']([^\"'#?]+)", html, flags=re.IGNORECASE)
    count = 0
    for href in links:
        if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#", "//")):
            continue
        count += 1
    return count


def page_type(path: Path) -> str:
    p = path.as_posix()
    if p.startswith("blog/"):
        return "blog"
    if p.startswith("guia/"):
        return "guia"
    if p.startswith("tools/"):
        return "tool"
    return "otros"


def main() -> int:
    html_files = sorted(p for p in ROOT.rglob("*.html") if p.name != "404.html")
    low_value: list[tuple[str, int, int, str]] = []

    for file_path in html_files:
        rel = file_path.relative_to(ROOT)
        html = file_path.read_text(encoding="utf-8", errors="ignore")
        words = extract_words(html)
        internal_links = count_internal_links(html)
        kind = page_type(rel)

        if kind in {"blog", "guia"} and (words < MIN_WORDS or internal_links < MIN_INTERNAL_LINKS):
            low_value.append((str(rel), words, internal_links, kind))

    print("== Content Value Audit ==")
    print(f"Umbral palabras (blog/guía): {MIN_WORDS}")
    print(f"Umbral enlaces internos (blog/guía): {MIN_INTERNAL_LINKS}")
    print(f"Páginas candidatas a mejorar: {len(low_value)}")

    for rel, words, links, kind in low_value[:80]:
        print(f" - [{kind}] {rel}: {words} palabras, {links} enlaces internos")

    print("\nSugerencia: prioriza primero blog/guías con pocas palabras y enlazado interno débil.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
