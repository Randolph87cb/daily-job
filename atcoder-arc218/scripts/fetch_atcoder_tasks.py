from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Iterable

import requests
from lxml import html


ATCODER_BASE = "https://atcoder.jp"
SCRIPT_DIR = Path(__file__).resolve().parent
TURNDOWN_SCRIPT = SCRIPT_DIR / "atcoder_better_turndown.cjs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch English task statements from AtCoder tasks_print and save them as Markdown."
    )
    parser.add_argument("--contest", required=True, help="Contest ID, for example: arc218")
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="Directory where Markdown files will be written.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout in seconds. Default: 30",
    )
    return parser.parse_args()


def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip()


def remove_thematic_break_blocks(markdown: str) -> str:
    parts = re.split(r"(\n\s*\n+)", markdown)
    filtered: list[str] = []
    for part in parts:
        stripped = part.strip()
        if stripped in {"***", "* * *", "---", "- - -", "___", "_ _ _"}:
            continue
        filtered.append(part)
    cleaned = "".join(filtered)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def task_slug(contest: str, short_code: str) -> str:
    return f"{contest}_{short_code.lower()}"


def fetch_html(contest: str, timeout: int) -> str:
    url = f"{ATCODER_BASE}/contests/{contest}/tasks_print?lang=en"
    response = requests.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AtCoderStatementFetcher/1.0)",
        },
    )
    response.raise_for_status()
    return response.text


def html_fragment_to_markdown(fragment_html: str) -> str:
    payload = json.dumps({"html": fragment_html}, ensure_ascii=False)
    result = subprocess.run(
        ["node", str(TURNDOWN_SCRIPT)],
        input=payload,
        text=True,
        capture_output=True,
        check=True,
        cwd=SCRIPT_DIR.parent,
    )
    return remove_thematic_break_blocks(result.stdout.strip())


def extract_tasks(page_html: str, contest: str) -> Iterable[tuple[str, str]]:
    root = html.fromstring(page_html)
    titles = root.xpath("//span[contains(@class,'h2')]")
    statements = root.xpath("//div[@id='task-statement']")

    if len(titles) != len(statements):
        raise RuntimeError(
            f"Title count ({len(titles)}) does not match statement count ({len(statements)})."
        )

    for title_node, statement_node in zip(titles, statements, strict=True):
        title = normalize_text("".join(title_node.itertext()))
        short_code = title.split(" - ", 1)[0]
        slug = task_slug(contest, short_code)
        source_url = f"{ATCODER_BASE}/contests/{contest}/tasks/{slug}?lang=en"

        english_nodes = statement_node.xpath(".//span[contains(@class,'lang-en')]")
        if not english_nodes:
            raise RuntimeError(f"Missing English statement for task {title}.")

        english_html = html.tostring(english_nodes[0], encoding="unicode")
        statement_markdown = html_fragment_to_markdown(english_html)
        parts = [f"# {title}", f"Source: {source_url}", statement_markdown]
        markdown = "\n\n".join(part for part in parts if part).strip() + "\n"
        yield slug, markdown


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    page_html = fetch_html(args.contest, args.timeout)
    for slug, markdown in extract_tasks(page_html, args.contest):
        output_path = args.output_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
