#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "catalog.json"


def read_yaml(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def collect(directory: pathlib.Path, key: str) -> list[dict]:
    result: list[dict] = []
    for path in sorted(directory.glob("*.yml")):
        result.extend((read_yaml(path) or {}).get(key, []))
    return result


def build_payload() -> dict:
    frameworks = read_yaml(ROOT / "knowledge" / "frameworks.yml").get("frameworks", [])
    actors = collect(ROOT / "knowledge" / "actors", "actors")
    threats = collect(ROOT / "knowledge" / "threats", "threats")

    items = []
    for x in frameworks:
        items.append({
            "id": x["id"],
            "name": x["name"],
            "type": "reference",
            "category": x["kind"],
            "scope": x["scope"],
            "status": x["status"],
            "source": x["source"],
        })

    for x in actors:
        items.append({
            "id": x["id"],
            "name": x["name"],
            "type": "actor",
            "category": x["type"],
            "scope": ", ".join(x.get("focus", [])),
            "status": x["status"],
            "source": x["source"],
            "region": x.get("region"),
            "confidence": x.get("confidence"),
            "featured": bool(x.get("featured", False)),
            "aliases": x.get("aliases", []),
        })

    for x in threats:
        items.append({
            "id": x["id"],
            "name": x["name"],
            "type": "threat",
            "category": x["class"],
            "scope": ", ".join(x.get("defensive_relevance", [])),
            "status": x["status"],
            "source": x["source"],
        })

    return {
        "version": "0.3",
        "count": len(items),
        "items": sorted(items, key=lambda x: (x["type"], x["name"].lower())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated catalog semantically with the committed catalog.",
    )
    args = parser.parse_args()
    payload = build_payload()

    if args.check:
        if not OUT.exists():
            print(f"ERROR: missing generated catalog: {OUT}")
            return 1
        with OUT.open("r", encoding="utf-8") as fh:
            committed = json.load(fh)

        def keyed(doc: dict) -> dict:
            return {
                (item["type"], item["id"]): item
                for item in doc.get("items", [])
            }

        same_header = (
            committed.get("version") == payload.get("version")
            and committed.get("count") == payload.get("count")
        )
        if not same_header or keyed(committed) != keyed(payload):
            print("ERROR: docs/data/catalog.json is stale.")
            return 1
        print(f"catalog is current ({payload['count']} items)")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT} ({payload['count']} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
