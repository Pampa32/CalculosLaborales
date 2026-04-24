#!/usr/bin/env python3
"""Validación rápida de SEO on-page para páginas HTML estáticas."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HTML_FILES = sorted(
    p for p in ROOT.rglob("*.html") if ".git" not in p.parts and "node_modules" not in p.parts
)

CHECKS = {
    "title": re.compile(r"<title\b", re.IGNORECASE),
    "meta_description": re.compile(
        r"<meta\b[^>]*name\s*=\s*['\"]description['\"][^>]*>", re.IGNORECASE
    ),
    "canonical": re.compile(
        r"<link\b[^>]*rel\s*=\s*['\"]canonical['\"][^>]*>", re.IGNORECASE
    ),
    "viewport": re.compile(
        r"<meta\b[^>]*name\s*=\s*['\"]viewport['\"][^>]*>", re.IGNORECASE
    ),
    "h1": re.compile(r"<h1\b", re.IGNORECASE),
}


def count(pattern: re.Pattern[str], text: str) -> int:
    return len(pattern.findall(text))


def main() -> int:
    if not HTML_FILES:
        print("No se encontraron archivos HTML.")
        return 1

    errors: list[str] = []

    for file_path in HTML_FILES:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        rel = file_path.relative_to(ROOT)

        title_count = count(CHECKS["title"], content)
        if title_count != 1:
            errors.append(f"{rel}: <title> esperado 1, encontrado {title_count}")

        desc_count = count(CHECKS["meta_description"], content)
        if desc_count != 1:
            errors.append(
                f"{rel}: meta description esperada 1, encontrada {desc_count}"
            )

        canonical_count = count(CHECKS["canonical"], content)
        if canonical_count != 1:
            errors.append(f"{rel}: canonical esperado 1, encontrado {canonical_count}")

        viewport_count = count(CHECKS["viewport"], content)
        if viewport_count != 1:
            errors.append(f"{rel}: viewport esperado 1, encontrado {viewport_count}")

        h1_count = count(CHECKS["h1"], content)
        if h1_count < 1:
            errors.append(f"{rel}: falta <h1>")

    if errors:
        print("❌ Validación SEO fallida. Problemas encontrados:")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"✅ Validación SEO correcta en {len(HTML_FILES)} archivos HTML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
