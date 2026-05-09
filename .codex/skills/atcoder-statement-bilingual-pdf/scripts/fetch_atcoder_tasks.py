from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Iterable

import requests
from lxml import html

try:
    import browser_cookie3
except ImportError:
    browser_cookie3 = None


ATCODER_BASE = "https://atcoder.jp"
SCRIPT_DIR = Path(__file__).resolve().parent
TURNDOWN_SCRIPT = SCRIPT_DIR / "atcoder_better_turndown.cjs"
BROWSER_COOKIE_ORDER = ["chrome", "edge", "brave", "chromium", "firefox", "opera", "vivaldi"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch English task statements from AtCoder tasks_print with browser login state and save them as Markdown."
    )
    parser.add_argument("contest", nargs="?", help="Contest ID, for example: arc218")
    parser.add_argument("--contest-id", dest="contest_flag", help="Legacy contest flag.")
    parser.add_argument(
        "--output-dir",
        default=None,
        type=Path,
        help="Directory where Markdown files will be written. Default: ./atcoder-output/<contest>/en",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout in seconds. Default: 30",
    )
    parser.add_argument(
        "--browser-cookies",
        default="auto",
        help="Load cookies from a local browser profile. Default: auto. Supported: auto, chrome, edge, brave, chromium, firefox, opera, vivaldi.",
    )
    return parser.parse_args()


def resolve_contest_id(args: argparse.Namespace) -> str:
    contest = (args.contest or "").strip()
    legacy_contest = (args.contest_flag or "").strip()
    resolved = contest or legacy_contest
    if not resolved:
        raise SystemExit("Contest ID is required. Example: fetch_atcoder_tasks.py abc456")
    return resolved


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


def browser_cookie_loader_names(browser_name: str) -> list[str]:
    normalized = browser_name.strip().lower()
    if not normalized:
        return []
    if normalized == "auto":
        return BROWSER_COOKIE_ORDER
    return [normalized]


def load_browser_cookie_jar(
    browser_name: str,
    domain_name: str = "atcoder.jp",
) -> requests.cookies.RequestsCookieJar:
    cookie_jar = requests.cookies.RequestsCookieJar()
    loader_names = browser_cookie_loader_names(browser_name)
    if not loader_names:
        return cookie_jar

    if browser_cookie3 is None:
        raise RuntimeError(
            "browser-cookie3 is not installed. Run `python -m pip install browser-cookie3` first."
        )

    errors: list[str] = []
    for loader_name in loader_names:
        loader = getattr(browser_cookie3, loader_name, None)
        if loader is None:
            errors.append(f"{loader_name}: unsupported browser name")
            continue
        try:
            loaded = loader(
                domain_name=domain_name,
            )
            cookie_jar.update(loaded)
            if len(cookie_jar) > 0:
                return cookie_jar
            errors.append(f"{loader_name}: no matching cookies found for {domain_name}")
        except Exception as exc:
            errors.append(f"{loader_name}: {type(exc).__name__}: {exc}")

    raise RuntimeError("Failed to load browser cookies. " + " | ".join(errors))


def fetch_html(
    contest: str,
    timeout: int,
    browser_cookies: str = "auto",
) -> str:
    url = f"{ATCODER_BASE}/contests/{contest}/tasks_print?lang=en"
    session = requests.Session()
    session.cookies.update(load_browser_cookie_jar(browser_cookies))
    response = session.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AtCoderStatementFetcher/1.0)",
            "Referer": f"{ATCODER_BASE}/contests/{contest}",
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
    contest_id = resolve_contest_id(args)
    output_dir = args.output_dir or (Path.cwd() / "atcoder-output" / contest_id / "en")
    output_dir.mkdir(parents=True, exist_ok=True)

    page_html = fetch_html(
        contest_id,
        args.timeout,
        browser_cookies=args.browser_cookies,
    )
    for slug, markdown in extract_tasks(page_html, contest_id):
        output_path = output_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
