#!/usr/bin/env python3
"""Auditoría general rápida antes de subir a hosting."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def run_check(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (proc.stdout + proc.stderr).strip()
    return proc.returncode, out


def check_internal_links() -> list[str]:
    errors: list[str] = []
    pattern = re.compile(r"(?:href|src)=['\"]([^'\"#?]+)", re.IGNORECASE)

    for html_file in sorted(ROOT.rglob("*.html")):
        text = html_file.read_text(encoding="utf-8", errors="ignore")
        for m in pattern.finditer(text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")):
                continue

            target = ROOT / url.lstrip("/") if url.startswith("/") else html_file.parent / url
            if not target.exists():
                rel = html_file.relative_to(ROOT)
                errors.append(f"{rel}: recurso local no encontrado -> {url}")

    return errors


def check_sitemap_coverage() -> tuple[list[str], list[str]]:
    sitemap = ROOT / "sitemap.xml"
    tree = ET.parse(sitemap)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = {el.text or "" for el in tree.findall(".//s:loc", ns)}

    html_paths = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel == "404.html":
            continue
        if rel.endswith("/index.html"):
            rel = rel[: -len("index.html")]
        elif rel == "index.html":
            rel = ""
        html_paths.append(rel)

    expected = {f"https://calculoslaborales.es/{p}" for p in html_paths}
    missing = sorted(expected - locs)
    extra = sorted(locs - expected)
    return missing, extra


def main() -> int:
    print("== Predeploy Audit ==")

    rc_seo, out_seo = run_check([sys.executable, "scripts/seo_guard.py"])
    print("\n[SEO guard]")
    print(out_seo)

    rc_ads, out_ads = run_check([sys.executable, "scripts/adsense_readiness.py"])
    print("\n[AdSense readiness]")
    print(out_ads)

    print("\n[Links internos]")
    link_errors = check_internal_links()
    if link_errors:
        print("❌ Enlaces rotos detectados:")
        for err in link_errors[:30]:
            print(f" - {err}")
    else:
        print("✅ No se detectaron enlaces internos rotos.")

    print("\n[Sitemap coverage]")
    missing, extra = check_sitemap_coverage()
    if missing:
        print(f"⚠️ URLs HTML no incluidas en sitemap: {len(missing)}")
        for m in missing[:15]:
            print(f" - {m}")
    else:
        print("✅ Todas las páginas HTML están en sitemap.")

    if extra:
        print(f"⚠️ URLs en sitemap que no existen como HTML directo: {len(extra)}")
        for e in extra[:15]:
            print(f" - {e}")

    if rc_seo != 0 or rc_ads != 0 or link_errors:
        print("\n❌ Estado final: NO listo para deploy.")
        return 1

    print("\n✅ Estado final: listo para deploy (con advertencias no bloqueantes, si las hay).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
