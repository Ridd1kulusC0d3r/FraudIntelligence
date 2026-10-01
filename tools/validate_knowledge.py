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


def validate_registry_files(
    paths: list[pathlib.Path],
    key: str,
    required: set[str],
) -> list[str]:
    errors: list[str] = []
    seen: dict[str, pathlib.Path] = {}

    for path in paths:
        data = load_yaml(path) or {}
        for index, item in enumerate(data.get(key, [])):
            missing = sorted(required - set(item))
            if missing:
                errors.append(f"{path}:{index}: missing {missing}")

            item_id = item.get("id")
            if item_id in seen:
                errors.append(
                    f"{path}:{index}: duplicate id {item_id}; first seen in {seen[item_id]}"
                )
            elif item_id:
                seen[item_id] = path

            source = item.get("source")
            if source and not source.startswith("https://"):
                errors.append(f"{path}:{index}: source must use https")

    return errors


def validate_requirements() -> list[str]:
    path = ROOT / "knowledge" / "intelligence-requirements.yml"
    data = load_yaml(path) or {}
    required = {
        "id", "title", "priority", "status", "decision_supported",
        "key_questions", "collection_requirements", "outputs"
    }
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(data.get("requirements", [])):
        missing = sorted(required - set(item))
        if missing:
            errors.append(f"{path}:{index}: missing {missing}")
        item_id = item.get("id")
        if item_id in seen:
            errors.append(f"{path}:{index}: duplicate id {item_id}")
        seen.add(item_id)
    return errors


def main() -> int:
    errors = validate_yaml_files()
    errors.extend(validate_json_schemas())

    errors.extend(validate_registry_files(
        [ROOT / "knowledge" / "frameworks.yml"],
        "frameworks",
        {"id","name","kind","scope","status","source","source_class","confidence"},
    ))

    errors.extend(validate_registry_files(
        sorted((ROOT / "knowledge" / "actors").glob("*.yml")),
        "actors",
        {"id","name","type","region","status","confidence","source"},
    ))

    errors.extend(validate_registry_files(
        sorted((ROOT / "knowledge" / "threats").glob("*.yml")),
        "threats",
        {"id","name","class","status","confidence","source"},
    ))

    errors.extend(validate_requirements())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("FraudIntelligence knowledge validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
