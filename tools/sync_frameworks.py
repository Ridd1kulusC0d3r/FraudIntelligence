#!/usr/bin/env python3
"""Download source-native public framework data without rewriting semantics."""

from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "upstream"

SOURCES = {
    "mitre-f3-v1.2": "https://raw.githubusercontent.com/center-for-threat-informed-defense/fight-fraud-framework/main/public/f3-v1.2.json",
    "stripe-ft3-tactics": "https://raw.githubusercontent.com/stripe/ft3/main/FT3_Tactics.json",
    "stripe-ft3-techniques": "https://raw.githubusercontent.com/stripe/ft3/main/FT3_Techniques.json",
}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "FraudIntelligence-sync/0.2"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": {},
    }

    for name, url in SOURCES.items():
        body = fetch(url)
        # Ensure JSON before writing.
        json.loads(body.decode("utf-8"))
        path = CACHE / f"{name}.json"
        path.write_bytes(body)
        manifest["sources"][name] = {
            "url": url,
            "sha256": hashlib.sha256(body).hexdigest(),
            "bytes": len(body),
        }
        print(f"synced {name}: {len(body)} bytes")

    (CACHE / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"manifest: {CACHE / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
