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


def validate_frameworks() -> list[str]:
    errors: list[str] = []
    path = ROOT / "knowledge" / "frameworks.yml"
    data = load_yaml(path)
    required = {"id","name","kind","scope","status","source","source_class","confidence"}
    seen: set[str] = set()

    for index, item in enumerate(data.get("frameworks", [])):
        missing = sorted(required - set(item))
        if missing:
            errors.append(f"{path}:{index}: missing {missing}")
        item_id = item.get("id")
        if item_id in seen:
            errors.append(f"{path}:{index}: duplicate id {item_id}")
        seen.add(item_id)
        source = item.get("source", "")
        if source and not source.startswith("https://"):
            errors.append(f"{path}:{index}: source must use https")

    return errors


def validate_json_schema() -> list[str]:
    errors: list[str] = []
    schema_path = ROOT / "schemas" / "fraud-intel-object.schema.json"
    with schema_path.open("r", encoding="utf-8") as fh:
        schema = json.load(fh)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        errors.append(f"{schema_path}: invalid schema: {exc}")
    return errors


def validate_yaml_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.yml"):
        try:
            load_yaml(path)
        except Exception as exc:
            errors.append(f"{path}: YAML parse failed: {exc}")
    return errors


def main() -> int:
    errors = validate_yaml_files()
    errors.extend(validate_frameworks())
    errors.extend(validate_json_schema())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("FraudIntelligence knowledge validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
