#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_yaml(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def validate_yaml_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.yml"):
        if ".cache" in path.parts:
            continue
        try:
            load_yaml(path)
        except Exception as exc:
            errors.append(f"{path}: YAML parse failed: {exc}")
    return errors


def validate_json_schemas() -> list[str]:
    errors: list[str] = []
    for schema_path in (ROOT / "schemas").glob("*.schema.json"):
        try:
            with schema_path.open("r", encoding="utf-8") as fh:
                schema = json.load(fh)
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            errors.append(f"{schema_path}: invalid schema: {exc}")
    return errors


def validate_registry(path: pathlib.Path, key: str, required: set[str]) -> list[str]:
    errors: list[str] = []
    data = load_yaml(path) or {}
    seen: set[str] = set()

    for index, item in enumerate(data.get(key, [])):
        missing = sorted(required - set(item))
        if missing:
            errors.append(f"{path}:{index}: missing {missing}")
        item_id = item.get("id")
        if item_id in seen:
            errors.append(f"{path}:{index}: duplicate id {item_id}")
        seen.add(item_id)
        source = item.get("source")
        if source and not source.startswith("https://"):
            errors.append(f"{path}:{index}: source must use https")
    return errors


def main() -> int:
    errors = validate_yaml_files()
    errors.extend(validate_json_schemas())
    errors.extend(validate_registry(
        ROOT / "knowledge" / "frameworks.yml",
        "frameworks",
        {"id","name","kind","scope","status","source","source_class","confidence"},
    ))
    errors.extend(validate_registry(
        ROOT / "knowledge" / "actors" / "brazil-latam.yml",
        "actors",
        {"id","name","type","status","confidence","source"},
    ))
    errors.extend(validate_registry(
        ROOT / "knowledge" / "threats" / "brazil-latam.yml",
        "threats",
        {"id","name","class","status","confidence","source"},
    ))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("FraudIntelligence knowledge validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
