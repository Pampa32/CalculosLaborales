#!/usr/bin/env python3
"""Checklist técnica básica para monetización con Google AdSense."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.rglob("*.html"))

REQUIRED_FILES = [
    Path("ads.txt"),
    Path("legal/privacidad.html"),
    Path("legal/cookies.html"),
    Path("legal/aviso-legal.html"),
]

REQUIRED_SNIPPETS = {
    "cookie_consent": "assets/js/cookie-consent.min.js",
    "adsense_loader": "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js",
    "ads_safe": "assets/js/ads-safe.min.js",
}


def has_file(rel_path: Path) -> bool:
    file_path = ROOT / rel_path
    return file_path.exists() and file_path.is_file() and file_path.stat().st_size > 0


def main() -> int:
    print("== AdSense Readiness ==")

    missing_files: list[str] = []
    for rel in REQUIRED_FILES:
        if has_file(rel):
            print(f"✅ Archivo requerido: {rel}")
        else:
            print(f"❌ Archivo requerido ausente o vacío: {rel}")
            missing_files.append(str(rel))

    missing_by_snippet: dict[str, list[str]] = {k: [] for k in REQUIRED_SNIPPETS}

    for html_file in HTML_FILES:
        content = html_file.read_text(encoding="utf-8", errors="ignore")
        rel = html_file.relative_to(ROOT)
        for key, snippet in REQUIRED_SNIPPETS.items():
            if snippet not in content:
                missing_by_snippet[key].append(str(rel))

    for key, files in missing_by_snippet.items():
        covered = len(HTML_FILES) - len(files)
        print(f"\n{key}: {covered}/{len(HTML_FILES)} páginas")
        if files:
            print("⚠️  Pendientes (primeras 15):")
            for item in files[:15]:
                print(f" - {item}")

    if missing_files:
        print("\n❌ Faltan archivos legales/técnicos obligatorios.")
        return 1

    print("\n✅ Revisión completada. Si hay pendientes, prioriza su cobertura antes de escalar tráfico pagado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
