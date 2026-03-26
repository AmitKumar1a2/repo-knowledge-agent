from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


QUESTION_PATTERN = re.compile(r"^## Q:\s*(.+?)\s*$", re.MULTILINE)
REPO_ROOT = Path(__file__).resolve().parents[3]
DAILY_DIR = REPO_ROOT / "docs" / "daily"


@dataclass(frozen=True)
class KnowledgeEntry:
    question: str
    answer: str
    entry_type: str
    tags: list[str]

    def render(self) -> str:
        return (
            f"## Q: {self.question}\n"
            f"**A:** {self.answer}\n\n"
            f"**Type:** {self.entry_type}\n"
            f"**Tags:** {', '.join(self.tags)}\n"
            f"**Source:** codex conversation\n\n"
            "---\n"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a conceptual knowledge entry to a daily markdown file."
    )
    parser.add_argument("--question", required=True, help="Rewritten reusable question.")
    parser.add_argument("--answer", required=True, help="Concise reusable answer.")
    parser.add_argument(
        "--type",
        required=True,
        dest="entry_type",
        choices=("CONCEPTUAL", "HYBRID"),
        help="Entry classification.",
    )
    parser.add_argument(
        "--tags",
        required=True,
        help="Comma-separated list of 2-5 tags.",
    )
    parser.add_argument(
        "--date",
        help="Target date in YYYY-MM-DD format. Defaults to today.",
    )
    return parser.parse_args()


def parse_target_date(raw_date: str | None) -> date:
    if raw_date is None:
        return date.today()
    try:
        return datetime.strptime(raw_date, "%Y-%m-%d").date()
    except ValueError as exc:
        raise SystemExit(f"Invalid --date '{raw_date}'. Expected YYYY-MM-DD.") from exc


def normalize_question(question: str) -> str:
    return " ".join(question.strip().lower().split())


def parse_tags(raw_tags: str) -> list[str]:
    tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
    unique_tags: list[str] = []
    seen: set[str] = set()

    for tag in tags:
        lowered = tag.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        unique_tags.append(tag)

    if not 2 <= len(unique_tags) <= 5:
        raise SystemExit("Expected --tags to contain 2-5 unique comma-separated values.")

    return unique_tags


def target_file_path(target_date: date) -> Path:
    return DAILY_DIR / f"{target_date.isoformat()}_Knowledge_Base.md"


def ensure_daily_file(file_path: Path, target_date: date) -> None:
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.write_text(
            f"# Knowledge Base - {target_date.isoformat()}\n",
            encoding="utf-8",
        )


def extract_normalized_questions(content: str) -> set[str]:
    return {normalize_question(match) for match in QUESTION_PATTERN.findall(content)}


def append_entry(file_path: Path, entry: KnowledgeEntry) -> bool:
    content = file_path.read_text(encoding="utf-8")
    if normalize_question(entry.question) in extract_normalized_questions(content):
        return False

    separator = "" if content.endswith("\n\n") or content == "" else "\n\n"
    with file_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(separator)
        handle.write(entry.render())
    return True


def main() -> None:
    args = parse_args()
    target_date = parse_target_date(args.date)
    file_path = target_file_path(target_date)
    ensure_daily_file(file_path, target_date)

    entry = KnowledgeEntry(
        question=args.question.strip(),
        answer=args.answer.strip(),
        entry_type=args.entry_type,
        tags=parse_tags(args.tags),
    )

    if append_entry(file_path, entry):
        print(f"Appended entry to {file_path}")
    else:
        print(f"Skipped duplicate question in {file_path}")


if __name__ == "__main__":
    main()
