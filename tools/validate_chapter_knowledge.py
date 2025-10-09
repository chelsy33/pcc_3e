"""Utility script to validate chapter knowledge coverage and annotate examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "learning_resources" / "chapter_knowledge_points.json"


class KnowledgePointError(RuntimeError):
    """Raised when a knowledge point can't be validated."""


def load_config() -> Dict[str, Dict]:
    if not CONFIG_PATH.exists():
        raise KnowledgePointError(f"Missing configuration file: {CONFIG_PATH}")
    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def ensure_comment(example_path: Path, comment: str) -> bool:
    """Ensure the example file starts with the desired comment.

    Returns True if the file was modified.
    """

    if not example_path.exists():
        raise KnowledgePointError(f"Example file not found: {example_path}")

    original_text = example_path.read_text(encoding="utf-8")
    lines = original_text.splitlines()

    # Find the first non-empty, non-shebang line.
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1

    # Handle shebangs by skipping them before inserting the comment.
    if index < len(lines) and lines[index].startswith("#!"):
        index += 1
        while index < len(lines) and not lines[index].strip():
            index += 1

    comment_line = comment.strip()
    updated = False

    if index < len(lines) and lines[index].startswith("#"):
        if lines[index].strip() != comment_line:
            lines[index] = comment_line
            updated = True
    else:
        insertion_index = index
        lines.insert(insertion_index, comment_line)
        if insertion_index + 1 < len(lines) and lines[insertion_index + 1].strip():
            lines.insert(insertion_index + 1, "")
        updated = True

    if updated:
        example_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return updated


def mirror_to_text_file(example_path: Path) -> None:
    """Mirror .py content to the paired .py.txt file when it exists."""

    txt_path = example_path.with_suffix(example_path.suffix + ".txt")
    if txt_path.exists():
        txt_path.write_text(example_path.read_text(encoding="utf-8"), encoding="utf-8")


def validate() -> None:
    config = load_config()
    missing_points: List[str] = []
    updates: List[Path] = []

    for chapter, chapter_info in sorted(config.items()):
        knowledge_points = chapter_info.get("knowledge_points", [])
        if not knowledge_points:
            missing_points.append(f"{chapter}: no knowledge points defined")
            continue
        for point in knowledge_points:
            point_id = point.get("id", "<unknown>")
            examples = point.get("examples", [])
            if not examples:
                missing_points.append(f"{chapter}.{point_id}: no examples provided")
                continue
            for example in examples:
                relative_path = example.get("path")
                comment = example.get("comment")
                if not relative_path or not comment:
                    missing_points.append(
                        f"{chapter}.{point_id}: example configuration incomplete"
                    )
                    continue
                example_path = REPO_ROOT / relative_path
                if ensure_comment(example_path, comment):
                    updates.append(example_path)
                mirror_to_text_file(example_path)

    if missing_points:
        raise KnowledgePointError("\n".join(missing_points))

    if updates:
        print("Updated comment headers for the following files:")
        for path in updates:
            print(f" - {path.relative_to(REPO_ROOT)}")
    else:
        print("All example files already contain the expected comments.")


if __name__ == "__main__":
    validate()
